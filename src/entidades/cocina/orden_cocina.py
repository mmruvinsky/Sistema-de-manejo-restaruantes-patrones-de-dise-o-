from datetime import datetime
from typing import Optional
from src.entidades.cocina.estado_orden import EstadoOrden
from src.entidades.pedidos.item_pedido import ItemPedido


class OrdenCocina:
    """Representa una orden individual en la cocina para un item específico"""
    
    _contador_id = 0
    
    def __init__(self, item_pedido: ItemPedido, pedido_id: int, mesa_id: Optional[int] = None):
        OrdenCocina._contador_id += 1
        self._id = OrdenCocina._contador_id
        self._item_pedido = item_pedido
        self._pedido_id = pedido_id
        self._mesa_id = mesa_id
        self._estado = EstadoOrden.PENDIENTE
        self._estacion_asignada = item_pedido.get_item_menu().get_estacion_cocina()
        self._prioridad = 1  # 1=normal, 2=alta, 3=urgente
        self._chef_asignado_id: Optional[int] = None
        
        # Tiempos
        self._fecha_hora_creacion = datetime.now()
        self._fecha_hora_inicio: Optional[datetime] = None
        self._fecha_hora_fin: Optional[datetime] = None
        
        # Observaciones
        self._notas_chef = ""
        self._observaciones_cliente = item_pedido.get_observaciones_especiales()
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_item_pedido(self) -> ItemPedido:
        return self._item_pedido
    
    def get_pedido_id(self) -> int:
        return self._pedido_id
    
    def get_mesa_id(self) -> Optional[int]:
        return self._mesa_id
    
    def get_estado(self) -> EstadoOrden:
        return self._estado
    
    def get_estacion_asignada(self) -> str:
        return self._estacion_asignada
    
    def get_prioridad(self) -> int:
        return self._prioridad
    
    def get_chef_asignado_id(self) -> Optional[int]:
        return self._chef_asignado_id
    
    def get_fecha_hora_creacion(self) -> datetime:
        return self._fecha_hora_creacion
    
    def get_notas_chef(self) -> str:
        return self._notas_chef
    
    def get_observaciones_cliente(self) -> str:
        return self._observaciones_cliente
    
    # --- SETTERS ---
    def set_prioridad(self, prioridad: int):
        """Establece la prioridad: 1=normal, 2=alta, 3=urgente"""
        if prioridad not in [1, 2, 3]:
            raise ValueError("La prioridad debe ser 1, 2 o 3")
        self._prioridad = prioridad
    
    def set_chef_asignado(self, chef_id: int):
        self._chef_asignado_id = chef_id
    
    def agregar_nota_chef(self, nota: str):
        """Agrega una nota del chef sobre la preparación"""
        if self._notas_chef:
            self._notas_chef += f"\n- {nota}"
        else:
            self._notas_chef = f"- {nota}"
    
    # --- GESTIÓN DE ESTADO ---
    def iniciar_preparacion(self):
        """Marca la orden como en preparación"""
        if self._estado != EstadoOrden.PENDIENTE:
            raise ValueError(f"No se puede iniciar una orden en estado {self._estado}")
        self._estado = EstadoOrden.EN_PREPARACION
        self._fecha_hora_inicio = datetime.now()
    
    def marcar_como_lista(self):
        """Marca la orden como lista para servir"""
        if self._estado != EstadoOrden.EN_PREPARACION:
            raise ValueError(f"No se puede marcar como lista una orden en estado {self._estado}")
        self._estado = EstadoOrden.LISTA
        self._fecha_hora_fin = datetime.now()
    
    def marcar_como_entregada(self):
        """Marca la orden como entregada al cliente"""
        if self._estado != EstadoOrden.LISTA:
            raise ValueError(f"No se puede entregar una orden en estado {self._estado}")
        self._estado = EstadoOrden.ENTREGADA
    
    def cancelar(self, motivo: str = ""):
        """Cancela la orden"""
        if self._estado == EstadoOrden.ENTREGADA:
            raise ValueError("No se puede cancelar una orden ya entregada")
        self._estado = EstadoOrden.CANCELADA
        if motivo:
            self.agregar_nota_chef(f"CANCELADA: {motivo}")
    
    # --- CÁLCULOS DE TIEMPO ---
    def calcular_tiempo_preparacion(self) -> Optional[int]:
        """Calcula el tiempo real de preparación en minutos"""
        if not self._fecha_hora_inicio or not self._fecha_hora_fin:
            return None
        delta = self._fecha_hora_fin - self._fecha_hora_inicio
        return int(delta.total_seconds() / 60)
    
    def calcular_tiempo_espera_actual(self) -> int:
        """Calcula el tiempo de espera desde la creación hasta ahora"""
        delta = datetime.now() - self._fecha_hora_creacion
        return int(delta.total_seconds() / 60)
    
    def get_tiempo_estimado(self) -> int:
        """Retorna el tiempo estimado de preparación del item"""
        return self._item_pedido.get_item_menu().get_tiempo_preparacion()
    
    def esta_retrasada(self) -> bool:
        """Verifica si la orden está retrasada respecto al tiempo estimado"""
        if self._estado in [EstadoOrden.LISTA, EstadoOrden.ENTREGADA, EstadoOrden.CANCELADA]:
            return False
        return self.calcular_tiempo_espera_actual() > self.get_tiempo_estimado()
    
    # --- VALIDACIONES ---
    def puede_iniciarse(self) -> bool:
        """Verifica si la orden puede iniciarse"""
        return self._estado == EstadoOrden.PENDIENTE and self._chef_asignado_id is not None
    
    def esta_en_progreso(self) -> bool:
        """Verifica si la orden está siendo preparada"""
        return self._estado == EstadoOrden.EN_PREPARACION
    
    def esta_completada(self) -> bool:
        """Verifica si la orden está completada (lista o entregada)"""
        return self._estado in [EstadoOrden.LISTA, EstadoOrden.ENTREGADA]
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado_emoji = {
            EstadoOrden.PENDIENTE: "⏳",
            EstadoOrden.EN_PREPARACION: "👨‍🍳",
            EstadoOrden.LISTA: "✅",
            EstadoOrden.ENTREGADA: "🍽️",
            EstadoOrden.CANCELADA: "❌"
        }
        
        prioridad_str = "🔴 URGENTE" if self._prioridad == 3 else "🟡 ALTA" if self._prioridad == 2 else "🟢 NORMAL"
        
        mesa_str = f"Mesa {self._mesa_id}" if self._mesa_id else "Para llevar"
        
        tiempo_info = ""
        if self._estado == EstadoOrden.EN_PREPARACION:
            tiempo_info = f"\n  ⏱️ Tiempo transcurrido: {self.calcular_tiempo_espera_actual()} min"
            if self.esta_retrasada():
                tiempo_info += " ⚠️ RETRASADA"
        elif self._fecha_hora_fin:
            tiempo_real = self.calcular_tiempo_preparacion()
            tiempo_info = f"\n  ✓ Tiempo de preparación: {tiempo_real} min"
        
        obs_cliente = f"\n  💬 Cliente: {self._observaciones_cliente}" if self._observaciones_cliente else ""
        notas_chef = f"\n  📝 Chef: {self._notas_chef}" if self._notas_chef else ""
        
        return (f"{estado_emoji.get(self._estado, '📋')} Orden #{self._id} - {prioridad_str}\n"
                f"  Pedido #{self._pedido_id} - {mesa_str}\n"
                f"  Item: {self._item_pedido.get_item_menu().get_nombre()} x{self._item_pedido.get_cantidad()}\n"
                f"  Estación: {self._estacion_asignada}\n"
                f"  Estado: {self._estado.value}\n"
                f"  Estimado: {self.get_tiempo_estimado()} min"
                f"{tiempo_info}"
                f"{obs_cliente}"
                f"{notas_chef}")
    
    def __repr__(self) -> str:
        return (f"OrdenCocina(id={self._id}, "
                f"pedido={self._pedido_id}, "
                f"estado={self._estado}, "
                f"estacion={self._estacion_asignada})")