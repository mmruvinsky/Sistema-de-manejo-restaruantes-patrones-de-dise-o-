from abc import ABC, abstractmethod
from typing import List
from src.patrones.observer.observer import IObserver

class IObservable(ABC):
    """
    Interfaz del Sujeto Observable.
    """
    
    @abstractmethod
    def agregar_observador(self, observador: IObserver):
        pass
        
    @abstractmethod
    def quitar_observador(self, observador: IObserver):
        pass
        
    @abstractmethod
    def notificar(self):
        pass

class Observable(IObservable):
    """
    Clase base concreta que implementa la lógica de
    manejo de observadores.
    
    Tus entidades (Ej. Ingrediente, Mesa) pueden heredar de aquí.
    """
    
    def __init__(self):
        self._observadores: List[IObserver] = []
        
    def agregar_observador(self, observador: IObserver):
        if observador not in self._observadores:
            self._observadores.append(observador)
            
    def quitar_observador(self, observador: IObserver):
        if observador in self._observadores:
            self._observadores.remove(observador)
            
    def notificar(self):
        """Notifica a todos los observadores en la lista"""
        for obs in self._observadores:
            obs.actualizar(self)