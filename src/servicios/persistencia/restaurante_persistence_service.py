import pickle
from typing import Any
from src.excepciones.persistencia_exception import PersistenciaException, ArchivoNoEncontradoException

class RestaurantePersistenceService:
    """
    Servicio Singleton para guardar y cargar el estado
    del restaurante (usando pickle como ejemplo).
    (Implementación placeholder)
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, archivo_data: str = "data/restaurante_estado.dat"):
        if hasattr(self, '_inicializado'):
            return
        self._archivo_data = archivo_data
        self._inicializado = True
        print(f"Servicio de Persistencia inicializado (archivo: {self._archivo_data})")
        
    def guardar_estado(self, data: Any):
        """Guarda un objeto (ej. un dict con todos los servicios) en un archivo."""
        try:
            with open(self._archivo_data, 'wb') as f:
                pickle.dump(data, f)
            print(f"Estado del restaurante guardado en {self._archivo_data}")
        except IOError as e:
            raise PersistenciaException("escritura", str(e))

    def cargar_estado(self) -> Any:
        """Carga el estado del restaurante desde un archivo."""
        try:
            with open(self._archivo_data, 'rb') as f:
                data = pickle.load(f)
            print(f"Estado del restaurante cargado desde {self._archivo_data}")
            return data
        except FileNotFoundError:
            raise ArchivoNoEncontradoException(self._archivo_data)
        except (IOError, pickle.PickleError) as e:
            raise PersistenciaException("lectura", str(e))