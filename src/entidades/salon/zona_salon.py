from enum import Enum

class ZonaSalon(Enum):
    """Zonas del salón"""
    INTERIOR = "Interior"
    TERRAZA = "Terraza"
    VIP = "VIP"
    BARRA = "Barra"
    
    def __str__(self):
        return self.value
