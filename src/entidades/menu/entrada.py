from src.entidades.menu.item_menu import ItemMenu
from src.constantes import PRECIO_BASE_ENTRADA, TIEMPO_PREPARACION_ENTRADA

class Entrada(ItemMenu):
    """Entradas/Aperitivos del menú"""
    
    def __init__(self, nombre: str, descripcion: str, tipo_entrada: str):
        super().__init__(
            nombre=nombre,
            descripcion=descripcion,
            precio_base=PRECIO_BASE_ENTRADA,
            tiempo_preparacion=TIEMPO_PREPARACION_ENTRADA
        )
        self._tipo_entrada = tipo_entrada  # "ensalada", "sopa", "tabla", etc.
    
    def calcular_precio_final(self) -> float:
        """Precio base sin modificaciones"""
        return self._precio_base
    
    def get_estacion_cocina(self) -> str:
        """Todas las entradas se preparan en la estación de cocina general"""
        return "Cocina"
    
    def get_tipo_entrada(self) -> str:
        return self._tipo_entrada