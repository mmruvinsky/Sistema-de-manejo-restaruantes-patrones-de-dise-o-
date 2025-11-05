"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/strategy
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 7
"""

# ================================================================================
# ARCHIVO 1/7: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/strategy/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/7: coccion_fritura_strategy.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/strategy/coccion_fritura_strategy.py
# ================================================================================

from src.patrones.strategy.metodo_coccion_strategy import IMetodoCoccionStrategy
from src.entidades.cocina.orden_cocina import OrdenCocina

class CoccionFrituraStrategy(IMetodoCoccionStrategy):
    """
    Estrategia concreta para cocinar por fritura.
    """
    def ejecutar_coccion(self, orden: OrdenCocina) -> str:
        item = orden.get_item_pedido().get_item_menu().get_nombre()
        mensaje = f"🍟 {item} preparado por Fritura."
        orden.agregar_nota_chef(mensaje)
        return mensaje

# ================================================================================
# ARCHIVO 3/7: coccion_horno_strategy.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/strategy/coccion_horno_strategy.py
# ================================================================================

from src.patrones.strategy.metodo_coccion_strategy import IMetodoCoccionStrategy
from src.entidades.cocina.orden_cocina import OrdenCocina

class CoccionHornoStrategy(IMetodoCoccionStrategy):
    """
    Estrategia concreta para cocinar al horno.
    """
    def ejecutar_coccion(self, orden: OrdenCocina) -> str:
        item = orden.get_item_pedido().get_item_menu().get_nombre()
        mensaje = f"🍞 {item} cocinado al Horno."
        orden.agregar_nota_chef(mensaje)
        return mensaje

# ================================================================================
# ARCHIVO 4/7: coccion_parrilla_strategy.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/strategy/coccion_parrilla_strategy.py
# ================================================================================

from src.patrones.strategy.metodo_coccion_strategy import IMetodoCoccionStrategy
from src.entidades.cocina.orden_cocina import OrdenCocina

class CoccionParrillaStrategy(IMetodoCoccionStrategy):
    """
    Estrategia concreta para cocinar a la parrilla.
    """
    def ejecutar_coccion(self, orden: OrdenCocina) -> str:
        item = orden.get_item_pedido().get_item_menu().get_nombre()
        # Aquí podría ir lógica más compleja, como verificar
        # el punto de cocción de la orden.
        mensaje = f"🔥 {item} cocinado a la Parrilla."
        orden.agregar_nota_chef(mensaje)
        return mensaje

# ================================================================================
# ARCHIVO 5/7: coccion_plancha_strategy.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/strategy/coccion_plancha_strategy.py
# ================================================================================

from src.patrones.strategy.metodo_coccion_strategy import IMetodoCoccionStrategy
from src.entidades.cocina.orden_cocina import OrdenCocina

class CoccionPlanchaStrategy(IMetodoCoccionStrategy):
    """
    Estrategia concreta para cocinar a la plancha.
    """
    def ejecutar_coccion(self, orden: OrdenCocina) -> str:
        item = orden.get_item_pedido().get_item_menu().get_nombre()
        mensaje = f"🍳 {item} cocinado a la Plancha."
        orden.agregar_nota_chef(mensaje)
        return mensaje

# ================================================================================
# ARCHIVO 6/7: coccion_vapor_strategy.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/strategy/coccion_vapor_strategy.py
# ================================================================================

from src.patrones.strategy.metodo_coccion_strategy import IMetodoCoccionStrategy
from src.entidades.cocina.orden_cocina import OrdenCocina

class CoccionVaporStrategy(IMetodoCoccionStrategy):
    """
    Estrategia concreta para cocinar al vapor.
    """
    def ejecutar_coccion(self, orden: OrdenCocina) -> str:
        item = orden.get_item_pedido().get_item_menu().get_nombre()
        mensaje = f"💨 {item} cocinado al Vapor."
        orden.agregar_nota_chef(mensaje)
        return mensaje

# ================================================================================
# ARCHIVO 7/7: metodo_coccion_strategy.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/strategy/metodo_coccion_strategy.py
# ================================================================================

from abc import ABC, abstractmethod
from src.entidades.cocina.orden_cocina import OrdenCocina

class IMetodoCoccionStrategy(ABC):
    """
    Interfaz abstracta (Patrón Strategy) para definir un método de cocción.
    """
    
    @abstractmethod
    def ejecutar_coccion(self, orden: OrdenCocina) -> str:
        """
        Ejecuta la lógica de cocción específica y retorna un
        mensaje del resultado.
        """
        pass
    
    def __str__(self):
        return self.__class__.__name__.replace("Coccion", "").replace("Strategy", "")

