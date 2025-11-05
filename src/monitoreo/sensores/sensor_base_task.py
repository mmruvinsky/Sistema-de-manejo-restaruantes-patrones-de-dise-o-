import threading
from abc import ABC, abstractmethod
from src.constantes import THREAD_JOIN_TIMEOUT

class SensorBase(threading.Thread, ABC):
    """
    Clase base abstracta para un sensor que corre en un hilo.
    """
    def __init__(self, intervalo_segundos: float):
        super().__init__(daemon=True)
        self._intervalo = intervalo_segundos
        self._stop_event = threading.Event()

    @abstractmethod
    def tomar_lectura(self):
        """
        Método abstracto que cada sensor implementará
        para tomar una lectura o simular un dato.
        """
        pass

    def run(self):
        """
        Método principal del hilo. Corre en bucle hasta que
        se llama a stop().
        """
        print(f"▶️ Iniciando sensor: {self.__class__.__name__}")
        while not self._stop_event.is_set():
            try:
                self.tomar_lectura()
            except Exception as e:
                print(f"Error en sensor {self.__class__.__name__}: {e}")
            
            self._stop_event.wait(self._intervalo)
        
        print(f"⏹️ Deteniendo sensor: {self.__class__.__name__}")

    def stop(self):
        """Señala al hilo que debe detenerse"""
        self._stop_event.set()
    
    def join_safe(self):
        """Intenta unirse al hilo de forma segura"""
        self.stop()
        super().join(THREAD_JOIN_TIMEOUT) #