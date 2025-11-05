from enum import Enum

class EstadoReserva(Enum):
    """Estados posibles de una reserva"""
    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    EN_CURSO = "En Curso"
    COMPLETADA = "Completada"
    CANCELADA = "Cancelada"
    NO_SHOW = "No Show"
    
    def __str__(self):
        return self.value