from enum import Enum

class NivelDeFidelidad(Enum):
    """Niveles de fidelidad para clientes frecuentes"""
    BRONCE = ("Bronce", 5, "🥉")      # nivel, descuento%, emoji
    PLATA = ("Plata", 10, "🥈")
    ORO = ("Oro", 15, "🥇")
    PLATINO = ("Platino", 20, "💎")
    
    def __init__(self, nombre: str, descuento: int, emoji: str):
        self._nombre_nivel = nombre
        self._descuento = descuento
        self._emoji = emoji
    
    @property
    def nombre_nivel(self) -> str:
        return self._nombre_nivel
    
    @property
    def descuento(self) -> int:
        """Porcentaje de descuento"""
        return self._descuento
    
    @property
    def emoji(self) -> str:
        return self._emoji
    
    def __str__(self):
        return f"{self._emoji} {self._nombre_nivel}"
    
    @classmethod
    def obtener_nivel_por_visitas(cls, cantidad_visitas: int):
        """Determina el nivel según la cantidad de visitas"""
        if cantidad_visitas >= 50:
            return cls.PLATINO
        elif cantidad_visitas >= 30:
            return cls.ORO
        elif cantidad_visitas >= 15:
            return cls.PLATA
        else:
            return cls.BRONCE