# src/entidades/pedidos/pedido.py

# --- IMPORTACIONES DE PATRONES ---
from src.patrones.state.pedido_state import IPedidoState
from src.patrones.state.pedido_recibidio_state import PedidoRecibidoState
# --- Faltaban estas importaciones para que la clase funcione ---
from src.patrones.state.pedido_listo_state import PedidoListoState
from src.patrones.state.pedido_servido_state import PedidoServidoState
# -------------------------------------------------------------
from src.patrones.decorator.precio_decorator import ICalculablePrecio
from src.entidades.pedidos.item_pedido import ItemPedido
from src.entidades.pedidos.estado_pedido import EstadoPedido
from src.entidades.pedidos.tipo_servicio import TipoServicio
from src.constantes import (
    DESCUENTO_CLIENTE_FRECUENTE,
    DESCUENTO_HAPPY_HOUR,
    RECARGO_DELIVERY,
    RECARGO_SERVICIO_MESA
)
from datetime import datetime
from typing import List, Optional

# La clase ahora implementa la interfaz ICalculablePrecio para el Decorator
class Pedido(ICalculablePrecio):
    """Representa un pedido completo del restaurante"""
    
    _contador_id = 0
    
    def __init__(self, cliente_id: int, mesa_id: Optional[int] = None, 
                 tipo_servicio: TipoServicio = TipoServicio.EN_SALON):
        Pedido._contador_id += 1
        self._id = Pedido._contador_id
        self._cliente_id = cliente_id
        self._mesa_id = mesa_id
        self._tipo_servicio = tipo_servicio
        self._items: List[ItemPedido] = []
        
        # --- CAMBIO A PATRÓN STATE ---
        # El estado ya no es un Enum, es un objeto de estado
        self._estado: IPedidoState = PedidoRecibidoState(self)
        # -----------------------------
        
        self._fecha_hora_pedido = datetime.now()
        self._fecha_hora_listo: Optional[datetime] = None
        self._fecha_hora_servido: Optional[datetime] = None
        self._mozo_id: Optional[int] = None
        self._observaciones = ""
        self._descuento_aplicado = 0.0
        self._recargo_aplicado = 0.0
        self._es_cliente_frecuente = False
        self._es_happy_hour = False
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_cliente_id(self) -> int:
        return self._cliente_id
    
    def get_mesa_id(self) -> Optional[int]:
        return self._mesa_id
        
    def get_tipo_servicio(self) -> TipoServicio:
        return self._tipo_servicio

    # --- MÉTODO AÑADIDO QUE FALTABA ---
    def get_items(self) -> List[ItemPedido]:
        """Retorna una copia de la lista de items del pedido"""
        return self._items.copy()
    # -------------------------------------
    
    def get_estado(self) -> IPedidoState:
        """Retorna el objeto de estado actual"""
        return self._estado

    # --- SETTERS ---

    # Este método es usado INTERNAMENTE por los objetos State
    def set_estado_interno(self, nuevo_estado: IPedidoState):
        """ Setter para que los estados puedan cambiar el estado del pedido """
        self._estado = nuevo_estado
        
        # Lógica de fechas que estaba en el setter anterior
        # (Asegúrate de tener importadas PedidoListoState y PedidoServidoState)
        if isinstance(nuevo_estado, PedidoListoState):
            self._fecha_hora_listo = datetime.now()
        elif isinstance(nuevo_estado, PedidoServidoState):
            self._fecha_hora_servido = datetime.now()

    def set_mozo_id(self, mozo_id: int):
        self._mozo_id = mozo_id
    
    def set_observaciones(self, observaciones: str):
        self._observaciones = observaciones
    
    def set_cliente_frecuente(self, es_frecuente: bool):
        self._es_cliente_frecuente = es_frecuente
    
    def set_happy_hour(self, es_happy_hour: bool):
        self._es_happy_hour = es_happy_hour
    
    # --- GESTIÓN DE ITEMS (Delegada al Estado) ---
    def agregar_item(self, item: ItemPedido):
        """Delega la lógica de agregar item al estado actual"""
        self._estado.agregar_item(item)
    
    def eliminar_item(self, item_id: int) -> bool:
        # La lógica de eliminar también debería ser manejada por el estado
        # (Omitido por brevedad, pero seguiría el mismo patrón que agregar_item)
        pass

    # --- CÁLCULOS (Implementa ICalculablePrecio) ---
    def calcular_subtotal(self) -> float:
        """Calcula el subtotal sin descuentos ni recargos"""
        return sum(item.calcular_precio_total() for item in self._items)
    
    def calcular_descuentos(self) -> float:
        # Esta lógica ahora será manejada por Decorators,
        # pero la dejamos como base.
        subtotal = self.calcular_subtotal()
        descuento_total = 0.0
        
        if self._es_cliente_frecuente:
            descuento_total += subtotal * (DESCUENTO_CLIENTE_FRECUENTE / 100)
        
        if self._es_happy_hour:
             descuento_total += subtotal * (DESCUENTO_HAPPY_HOUR / 100)
             
        return descuento_total

    def calcular_recargos(self) -> float:
        # Esta lógica ahora será manejada por Decorators
        recargo_total = self._recargo_aplicado
        
        if self._tipo_servicio == TipoServicio.DELIVERY:
            recargo_total += RECARGO_DELIVERY
        elif self._tipo_servicio == TipoServicio.EN_SALON:
             subtotal = self.calcular_subtotal()
             recargo_total += subtotal * (RECARGO_SERVICIO_MESA / 100)
             
        return recargo_total
    
    def calcular_total(self) -> float:
        """
        Calcula el total base. 
        Este es el método que será "envuelto" por los Decorators.
        """
        subtotal = self.calcular_subtotal()
        descuentos = self.calcular_descuentos()
        recargos = self.calcular_recargos()
        return subtotal - descuentos + recargos

    
    def aplicar_descuento_personalizado(self, porcentaje: float):
        """Aplica un descuento personalizado adicional"""
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El descuento debe estar entre 0 y 100")
        self._descuento_aplicado = porcentaje
    
    def aplicar_recargo_personalizado(self, monto: float):
        """Aplica un recargo personalizado adicional"""
        if monto < 0:
            raise ValueError("El recargo no puede ser negativo")
        self._recargo_aplicado = monto
    
    # --- TIEMPOS ---
    def calcular_tiempo_espera(self) -> Optional[int]:
        """Calcula el tiempo de espera en minutos desde que se hizo el pedido"""
        if self._fecha_hora_listo:
            delta = self._fecha_hora_listo - self._fecha_hora_pedido
            return int(delta.total_seconds() / 60)
        return None
    
    def calcular_tiempo_estimado_preparacion(self) -> int:
        """Calcula el tiempo estimado total de preparación"""
        if not self._items:
            return 0
        # Retorna el tiempo máximo entre todos los items
        return max(item.get_item_menu().get_tiempo_preparacion() 
                   for item in self._items)
    
    # --- VALIDACIONES ---
    def esta_completo(self) -> bool:
        """Verifica si el pedido tiene al menos un item"""
        return len(self._items) > 0
    
    def puede_cancelarse(self) -> bool:
        """Verifica si el pedido puede ser cancelado"""
        # Compara el tipo de estado (clase)
        return isinstance(self._estado, (PedidoRecibidoState)) # Solo Recibido
    
    def esta_listo(self) -> bool:
        """Verifica si el pedido está listo para servir"""
        return isinstance(self._estado, PedidoListoState)
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        # Usa el __str__ del objeto de estado
        estado_str = str(self._estado) 
        
        items_str = "\n".join([f"  - {item}" for item in self._items])
        
        return (f"\n📋 Pedido #{self._id}\n"
                f"Estado: {estado_str}\n"
                f"Tipo: {self._tipo_servicio.value}\n"
                f"Mesa: {self._mesa_id if self._mesa_id else 'N/A'}\n"
                f"Items:\n{items_str}\n"
                f"Subtotal: ${self.calcular_subtotal():.2f}\n"
                f"Descuentos: -${self.calcular_descuentos():.2f}\n"
                f"Recargos: +${self.calcular_recargos():.2f}\n"
                f"TOTAL: ${self.calcular_total():.2f}\n"
                f"Hora pedido: {self._fecha_hora_pedido.strftime('%H:%M:%S')}")
    
    def __repr__(self) -> str:
        return f"Pedido(id={self._id}, cliente={self._cliente_id}, estado={str(self._estado)})"
    
