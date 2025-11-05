from typing import List, Optional
from enum import Enum


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