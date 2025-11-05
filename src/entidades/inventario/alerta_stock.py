from datetime import datetime
from enum import Enum
from typing import Optional


class TipoAlerta(Enum):
    """Tipos de alertas de stock"""
    STOCK_BAJO = ("Stock Bajo", "🟡", 2)  # tipo, emoji, prioridad
    STOCK_CRITICO = ("Stock Crítico", "🟠", 3)
    AGOTADO = ("Agotado", "🔴", 5)
    POR_VENCER = ("Por Vencer", "⏰", 3)
    VENCIDO = ("Vencido", "⚠️", 5)
    SOBRESTOCK = ("Sobrestock", "📈", 1)
    
    def __init__(self, descripcion: str, emoji: str, prioridad: int):
        self._descripcion = descripcion
        self._emoji = emoji
        self._prioridad = prioridad
    
    @property
    def descripcion(self) -> str:
        return self._descripcion
    
    @property
    def emoji(self) -> str:
        return self._emoji
    
    @property
    def prioridad(self) -> int:
        """Prioridad de 1 (baja) a 5 (crítica)"""
        return self._prioridad
    
    def __str__(self):
        return f"{self._emoji} {self._descripcion}"


class AlertaStock:
    """Representa una alerta del sistema de inventario"""
    
    _contador_id = 0
    
    def __init__(self, ingrediente_id: int, ingrediente_nombre: str, 
                 tipo_alerta: TipoAlerta, mensaje: str):
        AlertaStock._contador_id += 1
        self._id = AlertaStock._contador_id
        self._ingrediente_id = ingrediente_id
        self._ingrediente_nombre = ingrediente_nombre
        self._tipo_alerta = tipo_alerta
        self._mensaje = mensaje
        self._fecha_hora_generacion = datetime.now()
        self._resuelta = False
        self._fecha_hora_resolucion: Optional[datetime] = None
        self._accion_tomada = ""
        self._usuario_responsable_id: Optional[int] = None
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_ingrediente_id(self) -> int:
        return self._ingrediente_id
    
    def get_ingrediente_nombre(self) -> str:
        return self._ingrediente_nombre
    
    def get_tipo_alerta(self) -> TipoAlerta:
        return self._tipo_alerta
    
    def get_mensaje(self) -> str:
        return self._mensaje
    
    def get_fecha_hora_generacion(self) -> datetime:
        return self._fecha_hora_generacion
    
    def esta_resuelta(self) -> bool:
        return self._resuelta
    
    def get_fecha_hora_resolucion(self) -> Optional[datetime]:
        return self._fecha_hora_resolucion
    
    def get_accion_tomada(self) -> str:
        return self._accion_tomada
    
    def get_prioridad(self) -> int:
        """Retorna la prioridad de la alerta"""
        return self._tipo_alerta.prioridad
    
    # --- SETTERS ---
    def resolver(self, accion_tomada: str, usuario_id: Optional[int] = None):
        """Marca la alerta como resuelta"""
        if self._resuelta:
            raise ValueError("La alerta ya está resuelta")
        
        self._resuelta = True
        self._fecha_hora_resolucion = datetime.now()
        self._accion_tomada = accion_tomada
        self._usuario_responsable_id = usuario_id
    
    def reabrir(self):
        """Reabre una alerta resuelta"""
        if not self._resuelta:
            raise ValueError("La alerta no está resuelta")
        
        self._resuelta = False
        self._fecha_hora_resolucion = None
        self._accion_tomada = ""
        self._usuario_responsable_id = None
    
    # --- CÁLCULOS ---
    def calcular_tiempo_sin_resolver(self) -> int:
        """Calcula los minutos desde que se generó la alerta"""
        if self._resuelta:
            return 0
        delta = datetime.now() - self._fecha_hora_generacion
        return int(delta.total_seconds() / 60)
    
    def calcular_tiempo_resolucion(self) -> Optional[int]:
        """Calcula los minutos que tomó resolver la alerta"""
        if not self._resuelta or not self._fecha_hora_resolucion:
            return None
        delta = self._fecha_hora_resolucion - self._fecha_hora_generacion
        return int(delta.total_seconds() / 60)
    
    def es_critica(self) -> bool:
        """Verifica si la alerta es de prioridad crítica (4 o 5)"""
        return self._tipo_alerta.prioridad >= 4
    
    def es_antigua(self, horas_limite: int = 24) -> bool:
        """Verifica si la alerta lleva mucho tiempo sin resolver"""
        if self._resuelta:
            return False
        horas = self.calcular_tiempo_sin_resolver() / 60
        return horas > horas_limite
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado = "✅ Resuelta" if self._resuelta else "⏳ Pendiente"
        
        tiempo_info = ""
        if self._resuelta:
            tiempo_resol = self.calcular_tiempo_resolucion()
            if tiempo_resol is not None:
                tiempo_info = f"\n  ⏱️ Tiempo de resolución: {tiempo_resol} min"
                tiempo_info += f"\n  ✓ Acción: {self._accion_tomada}"
        else:
            minutos = self.calcular_tiempo_sin_resolver()
            tiempo_info = f"\n  ⏱️ Sin resolver: {minutos} min"
            if self.es_antigua():
                tiempo_info += " ⚠️ ANTIGUA"
        
        return (f"{self._tipo_alerta} - Alerta #{self._id}\n"
                f"  Ingrediente: {self._ingrediente_nombre}\n"
                f"  {self._mensaje}\n"
                f"  Estado: {estado}\n"
                f"  Prioridad: {self._tipo_alerta.prioridad}/5\n"
                f"  Generada: {self._fecha_hora_generacion.strftime('%d/%m/%Y %H:%M')}"
                f"{tiempo_info}")
    
    def __repr__(self) -> str:
        return (f"AlertaStock(id={self._id}, "
                f"tipo={self._tipo_alerta.descripcion}, "
                f"ingrediente='{self._ingrediente_nombre}', "
                f"resuelta={self._resuelta})")
    
    # --- COMPARACIÓN PARA ORDENAMIENTO ---
    def __lt__(self, other):
        """Permite ordenar alertas por prioridad (mayor prioridad primero)"""
        if not isinstance(other, AlertaStock):
            return NotImplemented
        return self._tipo_alerta.prioridad > other._tipo_alerta.prioridad