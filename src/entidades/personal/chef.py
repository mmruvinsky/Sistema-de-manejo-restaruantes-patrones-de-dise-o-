from typing import List, Optional
from src.entidades.personal.empleado import Empleado
from src.entidades.personal.especialidad_chef import EspecialidadChef

class Chef(Empleado):
    """Chef del restaurante"""
    
    def __init__(self, nombre: str, apellido: str, dni: str, 
                 telefono: str, email: str, salario_base: float,
                 especialidad: EspecialidadChef):
        super().__init__(nombre, apellido, dni, telefono, email, salario_base)
        self._especialidad = especialidad
        self._estacion_asignada: Optional[str] = None
        self._ordenes_preparadas = 0
        self._ordenes_rechazadas = 0
        self._certificaciones: List[str] = []
    
    # --- GETTERS ESPECÍFICOS ---
    def get_especialidad(self) -> EspecialidadChef:
        return self._especialidad
    
    def get_estacion_asignada(self) -> Optional[str]:
        return self._estacion_asignada
    
    def get_ordenes_preparadas(self) -> int:
        return self._ordenes_preparadas
    
    def get_certificaciones(self) -> List[str]:
        return self._certificaciones.copy()
    
    # --- SETTERS ESPECÍFICOS ---
    def set_estacion_asignada(self, estacion: str):
        self._estacion_asignada = estacion
    
    # --- OPERACIONES ---
    def registrar_orden_preparada(self):
        """Incrementa el contador de órdenes preparadas"""
        self._ordenes_preparadas += 1
    
    def registrar_orden_rechazada(self):
        """Incrementa el contador de órdenes rechazadas"""
        self._ordenes_rechazadas += 1
    
    def agregar_certificacion(self, certificacion: str):
        """Agrega una certificación al chef"""
        if certificacion not in self._certificaciones:
            self._certificaciones.append(certificacion)
    
    # --- CÁLCULOS ---
    def calcular_salario_total(self) -> float:
        """Salario base + bono por especialidad + bono por desempeño"""
        bono_especialidad = 0.0
        
        if self._especialidad == EspecialidadChef.CHEF_EJECUTIVO:
            bono_especialidad = self._salario_base * 0.5
        elif self._especialidad == EspecialidadChef.SOUS_CHEF:
            bono_especialidad = self._salario_base * 0.3
        else:
            bono_especialidad = self._salario_base * 0.15
        
        # Bono por desempeño (basado en evaluaciones)
        promedio = self.calcular_promedio_evaluaciones()
        bono_desempeno = 0.0
        if promedio >= 9.0:
            bono_desempeno = self._salario_base * 0.2
        elif promedio >= 8.0:
            bono_desempeno = self._salario_base * 0.1
        
        return self._salario_base + bono_especialidad + bono_desempeno
    
    def calcular_tasa_exito(self) -> float:
        """Calcula el porcentaje de órdenes exitosas"""
        total = self._ordenes_preparadas + self._ordenes_rechazadas
        if total == 0:
            return 100.0
        return (self._ordenes_preparadas / total) * 100
    
    def obtener_rol(self) -> str:
        return f"Chef ({self._especialidad})"
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        estacion = f"\n  Estación: {self._estacion_asignada}" if self._estacion_asignada else ""
        certs = f"\n  Certificaciones: {', '.join(self._certificaciones)}" if self._certificaciones else ""
        
        return (f"{base_str}\n"
                f"  Especialidad: {self._especialidad.value}\n"
                f"  Órdenes preparadas: {self._ordenes_preparadas}\n"
                f"  Tasa de éxito: {self.calcular_tasa_exito():.1f}%"
                f"{estacion}"
                f"{certs}")
