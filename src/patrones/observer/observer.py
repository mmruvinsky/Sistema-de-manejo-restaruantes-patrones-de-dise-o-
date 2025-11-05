from abc import ABC, abstractmethod

class IObserver(ABC):
    """
    Interfaz del Observador.
    """
    
    @abstractmethod
    def actualizar(self, observable: 'IObservable'):
        """
        Método llamado por el observable cuando su estado cambia.
        """
        pass