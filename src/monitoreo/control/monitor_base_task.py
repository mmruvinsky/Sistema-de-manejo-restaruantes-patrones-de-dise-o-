import threading
from abc import ABC, abstractmethod
import time
from src.constantes import THREAD_JOIN_TIMEOUT

class MonitorBase(threading.Thread, ABC):
    """
    Clase base abstracta para un monitor que corre en un hilo.
    """
    def __init__(self, intervalo_segundos: float):
        super().__init__(daemon=True)  # Daemons mueren si el hilo principal muere
        self._intervalo = intervalo_segundos
        self._stop_event = threading.Event()

    @abstractmethod
    def verificar_estado(self):
        """
        Método abstracto que cada monitor implementará
        para chequear lo que necesite.
        """
        pass

    def run(self):
        """
        Método principal del hilo. Corre en bucle hasta que
        se llama a stop().
        """
        print(f"▶️ Iniciando monitor: {self.__class__.__name__}")
        while not self._stop_event.is_set():
            try:
                self.verificar_estado()
            except Exception as e:
                print(f"Error en monitor {self.__class__.__name__}: {e}")
            
            # Esperar el intervalo (o hasta que el evento de stop se active)
            self._stop_event.wait(self._intervalo)
        
        print(f"⏹️ Deteniendo monitor: {self.__class__.__name__}")

    def stop(self):
        """Señala al hilo que debe detenerse"""
        self._stop_event.set()
    
    def join_safe(self):
        """Intenta unirse al hilo de forma segura"""
        self.stop()
        super().join(THREAD_JOIN_TIMEOUT) #