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