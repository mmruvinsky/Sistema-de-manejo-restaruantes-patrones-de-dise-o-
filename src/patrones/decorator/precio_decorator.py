from abc import ABC, abstractmethod

class ICalculablePrecio(ABC):
    """
    Interfaz Componente: Define la operación que será decorada.
    Tu clase 'Pedido' implementará esta interfaz.
    """
    @abstractmethod
    def calcular_subtotal(self) -> float:
        pass
        
    @abstractmethod
    def calcular_total(self) -> float:
        pass

class PrecioDecoratorBase(ICalculablePrecio):
    """
    Clase Decorador Abstracta.
    Mantiene una referencia al componente que envuelve.
    """
    def __init__(self, componente: ICalculablePrecio):
        self._componente = componente
    
    @property
    def componente(self) -> ICalculablePrecio:
        return self._componente
        
    def calcular_subtotal(self) -> float:
        # Delega al componente envuelto
        return self._componente.calcular_subtotal()

    @abstractmethod
    def calcular_total(self) -> float:
        # Delega al componente envuelto (las subclases lo modificarán)
        pass