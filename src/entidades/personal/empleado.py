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
