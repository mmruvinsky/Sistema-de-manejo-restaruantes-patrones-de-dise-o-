from src.entidades.menu.item_menu import ItemMenu
from src.constantes import PRECIO_BASE_POSTRE, TIEMPO_PREPARACION_POSTRE

class Postre(ItemMenu):
    """Postres del menú"""
    
    def __init__(self, nombre: str, descripcion: str, 
                 tipo_postre: str, temperatura: str):
        super().__init__(
            nombre=nombre,
            descripcion=descripcion,
            precio_base=PRECIO_BASE_POSTRE,
            tiempo_preparacion=TIEMPO_PREPARACION_POSTRE
        )
        self._tipo_postre = tipo_postre  # "torta", "helado", "flan", etc.
        self._temperatura = temperatura  # "frío", "caliente"
        self._contiene_alcohol = False
    
    def calcular_precio_final(self) -> float:
        """Precio base + recargo por alcohol"""
        precio = self._precio_base
        
        if self._contiene_alcohol:
            precio += 3.00
        
        return precio
    
    def get_estacion_cocina(self) -> str:
        """Todos los postres van a la estación de postres"""
        return "Postres"
    
    def set_contiene_alcohol(self, contiene: bool):
        self._contiene_alcohol = contiene
    
    def contiene_alcohol(self) -> bool:
        return self._contiene_alcohol
    
    def get_tipo_postre(self) -> str:
        return self._tipo_postre
    
    def get_temperatura(self) -> str:
        return self._temperatura