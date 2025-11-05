from typing import List, Dict, Optional
from src.entidades.inventario.ingrediente import Ingrediente
from src.patrones.observer.observer import IObserver

class InventarioService:
    """
    Servicio Singleton para gestionar el inventario de ingredientes.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._ingredientes: Dict[str, Ingrediente] = {}
        self._observadores_stock: List[IObserver] = []
        self._inicializado = True
        print("Servicio de Inventario inicializado.")
        
    def agregar_ingrediente(self, ingrediente: Ingrediente):
        """
        Agrega un nuevo ingrediente al inventario y le
        adjunta todos los observadores de stock (ej. Sensores).
        """
        if ingrediente.get_nombre() not in self._ingredientes:
            self._ingredientes[ingrediente.get_nombre()] = ingrediente
            # Adjuntar observadores existentes al nuevo ingrediente
            for obs in self._observadores_stock:
                ingrediente.agregar_observador(obs)
        else:
            # Si ya existe, solo suma el stock
            self.agregar_stock(ingrediente.get_nombre(), ingrediente.get_cantidad_actual())

    def get_ingrediente(self, nombre: str) -> Optional[Ingrediente]:
        return self._ingredientes.get(nombre)

    def consumir_stock(self, nombre: str, cantidad: float):
        ingrediente = self.get_ingrediente(nombre)
        if not ingrediente:
            raise ValueError(f"Ingrediente '{nombre}' no encontrado en inventario.")
        
        ingrediente.consumir_stock(cantidad) # Esto notificará a los observadores

    def agregar_stock(self, nombre: str, cantidad: float):
        ingrediente = self.get_ingrediente(nombre)
        if not ingrediente:
            raise ValueError(f"Ingrediente '{nombre}' no encontrado en inventario.")
            
        ingrediente.agregar_stock(cantidad) # Esto notificará a los observadores
        
    def registrar_observador_stock(self, observador: IObserver):
        """
        Registra un observador (ej. SensorStock) que será notificado
        CADA VEZ que CUALQUIER ingrediente cambie.
        """
        if observador not in self._observadores_stock:
            self._observadores_stock.append(observador)
            # Agrega este observador a todos los ingredientes ya existentes
            for ing in self._ingredientes.values():
                ing.agregar_observador(observador)