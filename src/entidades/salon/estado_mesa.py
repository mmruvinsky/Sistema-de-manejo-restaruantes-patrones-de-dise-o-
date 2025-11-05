from enum import Enum

class EstadoMesa(Enum):
    """Estados posibles de una mesa"""
    DISPONIBLE = "Disponible"
    OCUPADA = "Ocupada"
    RESERVADA = "Reservada"
    EN_LIMPIEZA = "En Limpieza"
    FUERA_DE_SERVICIO = "Fuera de Servicio"
    
    def __str__(self):
        return self.value