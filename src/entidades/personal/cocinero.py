from typing import List, Optional
from src.entidades.personal.empleado import Empleado

class Cocinero(Empleado):
    """Cocinero asistente"""
    
    def __init__(self, nombre: str, apellido: str, dni: str, 
                 telefono: str, email: str, salario_base: float):
        super().__init__(nombre, apellido, dni, telefono, email, salario_base)
        self._chef_supervisor_id: Optional[int] = None
        self._estacion_asignada: Optional[str] = None
        self._tareas_completadas = 0
    
    def set_chef_supervisor(self, chef_id: int):
        self._chef_supervisor_id = chef_id
    
    def set_estacion_asignada(self, estacion: str):
        self._estacion_asignada = estacion
    
    def registrar_tarea_completada(self):
        self._tareas_completadas += 1
    
    def calcular_salario_total(self) -> float:
        """Salario base + bono por productividad"""
        bono = 0.0
        if self._tareas_completadas > 100:
            bono = self._salario_base * 0.1
        return self._salario_base + bono
    
    def obtener_rol(self) -> str:
        return "Cocinero"
    
    def __str__(self) -> str:
        base_str = super().__str__()
        estacion = f"\n  Estación: {self._estacion_asignada}" if self._estacion_asignada else ""
        return (f"{base_str}\n"
                f"  Tareas completadas: {self._tareas_completadas}"
                f"{estacion}")
