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