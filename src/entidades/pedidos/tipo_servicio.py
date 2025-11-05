from enum import Enum

class TipoServicio(Enum):
    """Tipos de servicio disponibles"""
    EN_SALON = "En Salón"
    TERRAZA = "Terraza"
    VIP = "VIP"
    DELIVERY = "Delivery"
    PARA_LLEVAR = "Para Llevar"
    
    def __str__(self):
        return self.value