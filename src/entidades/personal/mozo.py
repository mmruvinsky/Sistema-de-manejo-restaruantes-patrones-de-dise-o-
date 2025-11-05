from typing import List, Optional
from src.entidades.personal.empleado import Empleado

class Mozo(Empleado):
    """Mozo del restaurante"""
    
    def __init__(self, nombre: str, apellido: str, dni: str, 
                 telefono: str, email: str, salario_base: float):
        super().__init__(nombre, apellido, dni, telefono, email, salario_base)
        self._mesas_asignadas: List[int] = []  # IDs de mesas
        self._propinas_acumuladas = 0.0
        self._pedidos_atendidos = 0
        self._zona_asignada: Optional[str] = None
    
    # --- GETTERS ESPECÍFICOS ---
    def get_mesas_asignadas(self) -> List[int]:
        return self._mesas_asignadas.copy()
    
    def get_propinas_acumuladas(self) -> float:
        return self._propinas_acumuladas
    
    def get_pedidos_atendidos(self) -> int:
        return self._pedidos_atendidos
    
    def get_zona_asignada(self) -> Optional[str]:
        return self._zona_asignada
    
    # --- SETTERS ESPECÍFICOS ---
    def set_zona_asignada(self, zona: str):
        self._zona_asignada = zona
    
    # --- OPERACIONES ---
    def asignar_mesa(self, mesa_id: int):
        """Asigna una mesa al mozo"""
        if mesa_id not in self._mesas_asignadas:
            self._mesas_asignadas.append(mesa_id)
    
    def desasignar_mesa(self, mesa_id: int):
        """Desasigna una mesa del mozo"""
        if mesa_id in self._mesas_asignadas:
            self._mesas_asignadas.remove(mesa_id)
    
    def registrar_propina(self, monto: float):
        """Registra una propina recibida"""
        if monto < 0:
            raise ValueError("La propina no puede ser negativa")
        self._propinas_acumuladas += monto
    
    def registrar_pedido_atendido(self):
        """Incrementa el contador de pedidos atendidos"""
        self._pedidos_atendidos += 1
    
    # --- CÁLCULOS ---
    def calcular_salario_total(self) -> float:
        """Salario base + 50% de propinas"""
        return self._salario_base + (self._propinas_acumuladas * 0.5)
    
    def calcular_promedio_propina(self) -> float:
        """Calcula el promedio de propina por pedido"""
        if self._pedidos_atendidos == 0:
            return 0.0
        return self._propinas_acumuladas / self._pedidos_atendidos
    
    def obtener_rol(self) -> str:
        return "Mozo"
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        zona = f"\n  Zona: {self._zona_asignada}" if self._zona_asignada else ""
        return (f"{base_str}\n"
                f"  Mesas asignadas: {len(self._mesas_asignadas)}\n"
                f"  Pedidos atendidos: {self._pedidos_atendidos}\n"
                f"  Propinas: ${self._propinas_acumuladas:.2f} (Promedio: ${self.calcular_promedio_propina():.2f})"
                f"{zona}")

