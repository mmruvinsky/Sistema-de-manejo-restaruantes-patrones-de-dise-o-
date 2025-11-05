from enum import Enum

class EstadoOrden(Enum):
    """Estados posibles de una orden en cocina"""
    PENDIENTE = "Pendiente"
    EN_PREPARACION = "En Preparación"
    LISTA = "Lista"
    ENTREGADA = "Entregada"
    CANCELADA = "Cancelada"
    
    def __str__(self):
        return self.value