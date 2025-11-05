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