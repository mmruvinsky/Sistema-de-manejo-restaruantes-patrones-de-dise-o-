from enum import Enum

class EstadoPedido(Enum):
    """Estados posibles de un pedido"""
    RECIBIDO = "Recibido"
    EN_PREPARACION = "En Preparación"
    LISTO = "Listo"
    SERVIDO = "Servido"
    CANCELADO = "Cancelado"
    
    def __str__(self):
        return self.value