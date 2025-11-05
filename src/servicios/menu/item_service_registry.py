from typing import Dict, Optional
from src.entidades.menu.item_menu import ItemMenu

class ItemServiceRegistry:
    """
    Patrón Registry (como Singleton) para mantener una
    referencia a todas las plantillas de ItemMenu disponibles.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._items_menu: Dict[str, ItemMenu] = {}
        self._inicializado = True
        print("Registro de Items de Menú inicializado.")

    def registrar_item(self, item: ItemMenu):
        if item.get_nombre() not in self._items_menu:
            self._items_menu[item.get_nombre()] = item
            
    def get_item_por_nombre(self, nombre: str) -> Optional[ItemMenu]:
        item = self._items_menu.get(nombre)
        if not item:
            raise ValueError(f"Item '{nombre}' no encontrado en el registro.")
        
        return item