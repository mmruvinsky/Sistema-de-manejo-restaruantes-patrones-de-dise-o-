"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/factory
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/factory/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: estacion_factory.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/factory/estacion_factory.py
# ================================================================================

# src/patrones/factory/estacion_factory.py

from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.entidades.cocina.estacion_parrilla import EstacionParrilla 
from src.entidades.cocina.estacion_pastas import EstacionPastas 
from src.entidades.cocina.estacion_postres import EstacionPostres 
from src.entidades.cocina.estacion_bebidas import EstacionBebidas 

# --- IMPORTACIÓN AÑADIDA ---
# Importamos la nueva clase CONCRETA
from src.entidades.cocina.estacion_cocina_general import EstacionCocinaGeneral
# (Asegúrate de que la ruta de importación sea correcta según dónde guardaste el archivo)


class EstacionFactory:
    """
    Patrón Simple Factory para crear instancias de EstacionCocina.
    """
    
    @staticmethod
    def crear_estacion(nombre_estacion: str) -> EstacionCocina:
        """
        Crea y retorna un objeto EstacionCocina basado en su nombre.
        
        El 'nombre_estacion' proviene de los métodos 
        get_estacion_cocina() de tus ItemMenu.
        """
        nombre_normalizado = nombre_estacion.lower()
        
        if nombre_normalizado == "parrilla":
            return EstacionParrilla()
        
        elif nombre_normalizado == "pastas":
            return EstacionPastas()
            
        elif nombre_normalizado == "postres":
            return EstacionPostres()
        
        elif nombre_normalizado == "bebidas":
            return EstacionBebidas()
        
        # --- LÍNEA CORREGIDA ---
        elif nombre_normalizado == "cocina":
            # Para 'Entrada' y ahora 'Pescado'
            return EstacionCocinaGeneral() # Usamos la clase concreta
        
        # El caso "plancha" se ha eliminado
        
        else:
            raise ValueError(f"Tipo de estación desconocida: {nombre_estacion}")

# ================================================================================
# ARCHIVO 3/3: item_menu_factory.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/factory/item_menu_factory.py
# ================================================================================

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

