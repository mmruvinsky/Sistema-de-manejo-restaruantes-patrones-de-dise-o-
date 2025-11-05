from src.entidades.menu.categoria_item import CategoriaItem
from src.entidades.menu.item_menu import ItemMenu
from src.entidades.menu.entrada import Entrada
from src.entidades.menu.plato_principal import PlatoPrincipal
from src.entidades.menu.postre import Postre
from src.entidades.menu.bebida import Bebida

class ItemMenuFactory:
    """
    Patrón Simple Factory para crear instancias de ItemMenu.
    """
    
    @staticmethod
    def crear_item(categoria: CategoriaItem, **kwargs) -> ItemMenu:
        """
        Crea y retorna un objeto ItemMenu basado en la categoría.
        'kwargs' debe contener los argumentos necesarios.
        """
        try:
            if categoria == CategoriaItem.ENTRADA:
                return Entrada(
                    nombre=kwargs['nombre'],
                    descripcion=kwargs['descripcion'],
                    tipo_entrada=kwargs['tipo_entrada']
                ) #
            
            elif categoria == CategoriaItem.PLATO_PRINCIPAL:
                return PlatoPrincipal(
                    nombre=kwargs['nombre'],
                    descripcion=kwargs['descripcion'],
                    tipo_proteina=kwargs['tipo_proteina'],
                    guarnicion=kwargs['guarnicion']
                ) #
            
            elif categoria == CategoriaItem.POSTRE:
                return Postre(
                    nombre=kwargs['nombre'],
                    descripcion=kwargs['descripcion'],
                    tipo_postre=kwargs['tipo_postre'],
                    temperatura=kwargs['temperatura']
                ) #
            
            elif categoria == CategoriaItem.BEBIDA:
                return Bebida(
                    nombre=kwargs['nombre'],
                    descripcion=kwargs['descripcion'],
                    tipo_bebida=kwargs['tipo_bebida'],
                    tamanio=kwargs.get('tamanio', 'mediano')
                ) #
            
            else:
                raise ValueError(f"Categoría de item desconocida: {categoria}")
        
        except KeyError as e:
            raise AttributeError(f"Falta el argumento '{e}' para crear un '{categoria}'")