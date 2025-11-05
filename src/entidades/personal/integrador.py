"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: cajero.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/cajero.py
# ================================================================================

from typing import List, Optional
from src.entidades.personal.empleado import Empleado

class Cajero(Empleado):
    """Cajero del restaurante"""
    
    def __init__(self, nombre: str, apellido: str, dni: str, 
                 telefono: str, email: str, salario_base: float):
        super().__init__(nombre, apellido, dni, telefono, email, salario_base)
        self._transacciones_procesadas = 0
        self._monto_total_procesado = 0.0
        self._caja_asignada: Optional[int] = None
    
    def set_caja_asignada(self, numero_caja: int):
        self._caja_asignada = numero_caja
    
    def registrar_transaccion(self, monto: float):
        """Registra una transacción procesada"""
        self._transacciones_procesadas += 1
        self._monto_total_procesado += monto
    
    def calcular_salario_total(self) -> float:
        """Salario base + bono por volumen"""
        bono = 0.0
        if self._transacciones_procesadas > 500:
            bono = self._salario_base * 0.15
        elif self._transacciones_procesadas > 300:
            bono = self._salario_base * 0.1
        return self._salario_base + bono
    
    def obtener_rol(self) -> str:
        return "Cajero"
    
    def __str__(self) -> str:
        base_str = super().__str__()
        caja = f"\n  Caja: #{self._caja_asignada}" if self._caja_asignada else ""
        return (f"{base_str}\n"
                f"  Transacciones: {self._transacciones_procesadas}\n"
                f"  Monto procesado: ${self._monto_total_procesado:.2f}"
                f"{caja}")

# ================================================================================
# ARCHIVO 3/8: chef.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/chef.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/8: cocinero.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/cocinero.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/8: empleado.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/empleado.py
# ================================================================================

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from src.entidades.personal.turno import Turno

class Empleado(ABC):
    """Clase base abstracta para todos los empleados"""
    
    _contador_id = 0
    
    def __init__(self, nombre: str, apellido: str, dni: str, 
                 telefono: str, email: str, salario_base: float):
        Empleado._contador_id += 1
        self._id = Empleado._contador_id
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._telefono = telefono
        self._email = email
        self._salario_base = salario_base
        self._fecha_contratacion = datetime.now()
        self._turno_asignado = Turno.COMPLETO
        self._activo = True
        self._dias_trabajados = 0
        self._evaluaciones: List[float] = []  # Calificaciones de desempeño
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_nombre_completo(self) -> str:
        return f"{self._nombre} {self._apellido}"
    
    def get_dni(self) -> str:
        return self._dni
    
    def get_telefono(self) -> str:
        return self._telefono
    
    def get_email(self) -> str:
        return self._email
    
    def get_salario_base(self) -> float:
        return self._salario_base
    
    def get_turno_asignado(self) -> Turno:
        return self._turno_asignado
    
    def esta_activo(self) -> bool:
        return self._activo
    
    def get_dias_trabajados(self) -> int:
        return self._dias_trabajados
    
    # --- SETTERS ---
    def set_turno_asignado(self, turno: Turno):
        self._turno_asignado = turno
    
    def set_activo(self, activo: bool):
        self._activo = activo
    
    def set_salario_base(self, salario: float):
        if salario <= 0:
            raise ValueError("El salario debe ser positivo")
        self._salario_base = salario
    
    # --- MÉTODOS ---
    def registrar_dia_trabajado(self):
        """Registra un día de trabajo"""
        self._dias_trabajados += 1
    
    def agregar_evaluacion(self, calificacion: float):
        """Agrega una evaluación de desempeño (0-10)"""
        if calificacion < 0 or calificacion > 10:
            raise ValueError("La calificación debe estar entre 0 y 10")
        self._evaluaciones.append(calificacion)
    
    def calcular_promedio_evaluaciones(self) -> float:
        """Calcula el promedio de evaluaciones"""
        if not self._evaluaciones:
            return 0.0
        return sum(self._evaluaciones) / len(self._evaluaciones)
    
    def calcular_antiguedad_dias(self) -> int:
        """Calcula la antigüedad en días"""
        delta = datetime.now() - self._fecha_contratacion
        return delta.days
    
    @abstractmethod
    def calcular_salario_total(self) -> float:
        """Calcula el salario total incluyendo bonos"""
        pass
    
    @abstractmethod
    def obtener_rol(self) -> str:
        """Retorna el rol del empleado"""
        pass
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado = "✅ Activo" if self._activo else "❌ Inactivo"
        promedio = self.calcular_promedio_evaluaciones()
        
        return (f"👤 {self.obtener_rol()}: {self.get_nombre_completo()}\n"
                f"  DNI: {self._dni}\n"
                f"  Estado: {estado}\n"
                f"  Turno: {self._turno_asignado}\n"
                f"  Salario: ${self._salario_base:.2f}\n"
                f"  Antigüedad: {self.calcular_antiguedad_dias()} días\n"
                f"  Evaluación promedio: {promedio:.1f}/10")
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self._id}, nombre='{self.get_nombre_completo()}')"


# ================================================================================
# ARCHIVO 6/8: especialidad_chef.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/especialidad_chef.py
# ================================================================================

# src/entidades/personal/especialidad_chef.py

from enum import Enum

class EspecialidadChef(Enum):
    """
    Define las especialidades y rangos de los chefs en la cocina.
    """
    
    # Rangos jerárquicos
    CHEF_EJECUTIVO = "Chef Ejecutivo"
    SOUS_CHEF = "Sous Chef"
    
    # Especialidades de estación
    PARRILLA = "Parrilla"
    PASTAS = "Pastas"
    REPOSTERIA = "Repostería"
    GARDE_MANGER = "Garde Manger (Fríos)"
    COCINA_GENERAL = "Cocina General"
    
    def __str__(self):
        """Retorna el valor legible de la especialidad."""
        return self.value

# ================================================================================
# ARCHIVO 7/8: mozo.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/mozo.py
# ================================================================================

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



# ================================================================================
# ARCHIVO 8/8: turno.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/personal/turno.py
# ================================================================================

from typing import List, Optional
from enum import Enum
from datetime import time


class Turno(Enum):
    """Turnos de trabajo"""
    MAÑANA = ("Mañana", time(6, 0), time(14, 0))
    TARDE = ("Tarde", time(14, 0), time(22, 0))
    NOCHE = ("Noche", time(22, 0), time(6, 0))
    COMPLETO = ("Completo", time(9, 0), time(21, 0))
    
    def __init__(self, nombre: str, hora_inicio: time, hora_fin: time):
        self._nombre_turno = nombre
        self._hora_inicio = hora_inicio
        self._hora_fin = hora_fin
    
    @property
    def nombre_turno(self) -> str:
        return self._nombre_turno
    
    @property
    def hora_inicio(self) -> time:
        return self._hora_inicio
    
    @property
    def hora_fin(self) -> time:
        return self._hora_fin
    
    def __str__(self):
        return f"{self._nombre_turno} ({self._hora_inicio.strftime('%H:%M')} - {self._hora_fin.strftime('%H:%M')})"

