from enum import Enum

class UnidadMedida(Enum):
    """Unidades de medida para ingredientes"""
    KILOGRAMOS = ("kg", "Kilogramos")
    GRAMOS = ("g", "Gramos")
    LITROS = ("L", "Litros")
    MILILITROS = ("mL", "Mililitros")
    UNIDADES = ("u", "Unidades")
    PORCIONES = ("porc", "Porciones")
    PAQUETES = ("paq", "Paquetes")
    
    def __init__(self, abreviatura: str, nombre_completo: str):
        self._abreviatura = abreviatura
        self._nombre_completo = nombre_completo
    
    @property
    def abreviatura(self) -> str:
        return self._abreviatura
    
    @property
    def nombre_completo(self) -> str:
        return self._nombre_completo
    
    def __str__(self):
        return self._abreviatura
    
    @classmethod
    def obtener_por_abreviatura(cls, abrev: str):
        """Busca una unidad por su abreviatura"""
        for unidad in cls:
            if unidad.abreviatura == abrev:
                return unidad
        return None