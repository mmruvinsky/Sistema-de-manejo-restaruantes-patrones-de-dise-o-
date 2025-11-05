from datetime import datetime
from typing import Optional
from src.entidades.salon.estado_mesa import EstadoMesa
from src.entidades.salon.zona_salon import ZonaSalon

class Mesa:
    """Representa una mesa del restaurante"""
    
    _contador_id = 0
    
    def __init__(self, numero: int, capacidad: int, zona: ZonaSalon):
        Mesa._contador_id += 1
        self._id = Mesa._contador_id
        self._numero = numero
        self._capacidad = capacidad
        self._zona = zona
        self._estado = EstadoMesa.DISPONIBLE
        self._comensales_actuales = 0
        self._mozo_asignado_id: Optional[int] = None
        self._pedido_actual_id: Optional[int] = None
        self._reserva_actual_id: Optional[int] = None
        self._fecha_hora_ocupacion: Optional[datetime] = None
        self._observaciones = ""
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_numero(self) -> int:
        return self._numero
    
    def get_capacidad(self) -> int:
        return self._capacidad
    
    def get_zona(self) -> ZonaSalon:
        return self._zona
    
    def get_estado(self) -> EstadoMesa:
        return self._estado
    
    def get_comensales_actuales(self) -> int:
        return self._comensales_actuales
    
    def get_mozo_asignado_id(self) -> Optional[int]:
        return self._mozo_asignado_id
    
    def get_pedido_actual_id(self) -> Optional[int]:
        return self._pedido_actual_id
    
    def get_reserva_actual_id(self) -> Optional[int]:
        return self._reserva_actual_id
    
    def get_observaciones(self) -> str:
        return self._observaciones
    
    # --- SETTERS ---
    def set_estado(self, estado: EstadoMesa):
        self._estado = estado
    
    def set_mozo_asignado(self, mozo_id: int):
        self._mozo_asignado_id = mozo_id
    
    def set_observaciones(self, observaciones: str):
        self._observaciones = observaciones
    
    # --- OPERACIONES ---
    def ocupar(self, cantidad_comensales: int, pedido_id: Optional[int] = None):
        """Marca la mesa como ocupada"""
        if self._estado != EstadoMesa.DISPONIBLE:
            raise ValueError(f"La mesa no está disponible (Estado: {self._estado})")
        
        if cantidad_comensales > self._capacidad:
            raise ValueError(f"Cantidad de comensales ({cantidad_comensales}) excede capacidad ({self._capacidad})")
        
        self._estado = EstadoMesa.OCUPADA
        self._comensales_actuales = cantidad_comensales
        self._pedido_actual_id = pedido_id
        self._fecha_hora_ocupacion = datetime.now()
    
    def liberar(self):
        """Libera la mesa"""
        if self._estado != EstadoMesa.OCUPADA:
            raise ValueError("La mesa no está ocupada")
        
        self._estado = EstadoMesa.EN_LIMPIEZA
        self._comensales_actuales = 0
        self._pedido_actual_id = None
        self._fecha_hora_ocupacion = None
    
    def marcar_disponible(self):
        """Marca la mesa como disponible después de limpieza"""
        self._estado = EstadoMesa.DISPONIBLE
        self._reserva_actual_id = None
    
    def reservar(self, reserva_id: int):
        """Marca la mesa como reservada"""
        if self._estado != EstadoMesa.DISPONIBLE:
            raise ValueError("La mesa no está disponible para reservar")
        
        self._estado = EstadoMesa.RESERVADA
        self._reserva_actual_id = reserva_id
    
    def cancelar_reserva(self):
        """Cancela la reserva de la mesa"""
        if self._estado != EstadoMesa.RESERVADA:
            raise ValueError("La mesa no está reservada")
        
        self._estado = EstadoMesa.DISPONIBLE
        self._reserva_actual_id = None
    
    def marcar_fuera_de_servicio(self, motivo: str):
        """Marca la mesa como fuera de servicio"""
        self._estado = EstadoMesa.FUERA_DE_SERVICIO
        self.set_observaciones(motivo)
    
    def poner_en_servicio(self):
        """Vuelve a poner la mesa en servicio"""
        self._estado = EstadoMesa.DISPONIBLE
        self._observaciones = ""
    
    # --- CÁLCULOS ---
    def calcular_tiempo_ocupacion(self) -> Optional[int]:
        """Retorna el tiempo de ocupación en minutos"""
        if not self._fecha_hora_ocupacion:
            return None
        delta = datetime.now() - self._fecha_hora_ocupacion
        return int(delta.total_seconds() / 60)
    
    def calcular_porcentaje_ocupacion(self) -> float:
        """Retorna el porcentaje de ocupación actual"""
        if self._comensales_actuales == 0:
            return 0.0
        return (self._comensales_actuales / self._capacidad) * 100
    
    # --- VALIDACIONES ---
    def esta_disponible(self) -> bool:
        return self._estado == EstadoMesa.DISPONIBLE
    
    def esta_ocupada(self) -> bool:
        return self._estado == EstadoMesa.OCUPADA
    
    def esta_reservada(self) -> bool:
        return self._estado == EstadoMesa.RESERVADA
    
    def puede_aceptar_comensales(self, cantidad: int) -> bool:
        """Verifica si la mesa puede aceptar X comensales"""
        return self.esta_disponible() and cantidad <= self._capacidad
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado_emoji = {
            EstadoMesa.DISPONIBLE: "🟢",
            EstadoMesa.OCUPADA: "🔴",
            EstadoMesa.RESERVADA: "🟡",
            EstadoMesa.EN_LIMPIEZA: "🧹",
            EstadoMesa.FUERA_DE_SERVICIO: "⚠️"
        }
        
        zona_emoji = {
            ZonaSalon.INTERIOR: "🏠",
            ZonaSalon.TERRAZA: "🌳",
            ZonaSalon.VIP: "👑",
            ZonaSalon.BARRA: "🍺"
        }
        
        ocupacion = ""
        if self._estado == EstadoMesa.OCUPADA:
            tiempo = self.calcular_tiempo_ocupacion()
            ocupacion = f"\n  👥 Comensales: {self._comensales_actuales}/{self._capacidad}\n  ⏱️ Tiempo: {tiempo} min"
        
        obs = f"\n  📝 {self._observaciones}" if self._observaciones else ""
        
        return (f"{estado_emoji.get(self._estado, '❓')} Mesa #{self._numero}\n"
                f"  {zona_emoji.get(self._zona, '')} Zona: {self._zona.value}\n"
                f"  Estado: {self._estado.value}\n"
                f"  Capacidad: {self._capacidad} personas"
                f"{ocupacion}"
                f"{obs}")
    
    def __repr__(self) -> str:
        return f"Mesa(numero={self._numero}, zona={self._zona}, estado={self._estado})"