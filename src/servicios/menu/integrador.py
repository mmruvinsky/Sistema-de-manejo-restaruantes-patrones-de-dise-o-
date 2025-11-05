"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/menu
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/menu/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: item_service_registry.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/menu/item_service_registry.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: menu_service.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/menu/menu_service.py
# ================================================================================

from src.patrones.factory.item_menu_factory import ItemMenuFactory
from src.servicios.menu.item_service_registry import ItemServiceRegistry
from src.entidades.menu.categoria_item import CategoriaItem
from src.entidades.menu.item_menu import ItemMenu

class MenuService:
    """
    Servicio Singleton que utiliza el Factory para crear
    items y los registra en el Registry.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._factory = ItemMenuFactory()
        self._registry = ItemServiceRegistry()
        self._inicializado = True
        print("Servicio de Menú inicializado.")

    def crear_y_registrar_item(self, categoria: CategoriaItem, **kwargs) -> ItemMenu:
        """
        Paso 1: Usa la Factory para crear el item.
        Paso 2: Usa el Registry para registrarlo.
        """
        try:
            item = self._factory.crear_item(categoria, **kwargs)
            self._registry.registrar_item(item)
            print(f"Item creado y registrado: {item.get_nombre()}")
            return item
        except (AttributeError, ValueError) as e:
            print(f"Error al crear item: {e}")
            raise
            
    def get_item_del_menu(self, nombre: str) -> ItemMenu:
        """
        Obtiene una plantilla de item desde el registro.
        """
        return self._registry.get_item_por_nombre(nombre)

