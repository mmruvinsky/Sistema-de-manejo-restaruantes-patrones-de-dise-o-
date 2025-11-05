from enum import Enum

class TipoCoccion(Enum):
    """Métodos de cocción disponibles en el restaurante"""
    PARRILLA = "Parrilla"
    PLANCHA = "Plancha"
    HORNO = "Horno"
    FRITURA = "Fritura"
    VAPOR = "Vapor"
    HERVIDO = "Hervido"
    CRUDO = "Crudo"  # Para ensaladas, ceviches, etc.
    
    @classmethod
    def valores_validos(cls):
        """Retorna lista de valores válidos"""
        return [e.value for e in cls]
    
    def __str__(self):
        return self.value