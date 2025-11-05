"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/control
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/control/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: monitor_base_task.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/control/monitor_base_task.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: monitor_cocina_task.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/control/monitor_cocina_task.py
# ================================================================================

from typing import List
from src.monitoreo.control.monitor_base_task import MonitorBase #
from src.entidades.cocina.estacion_cocina import EstacionCocina #
from src.entidades.cocina.estacion_parrilla import EstacionParrilla #
from src.entidades.cocina.estacion_bebidas import EstacionBebidas #
from src.entidades.cocina.estacion_pastas import EstacionPastas #

class MonitorCocina(MonitorBase):
    
    def __init__(self, estaciones: List[EstacionCocina], intervalo_segundos: float):
        super().__init__(intervalo_segundos)
        self._estaciones = estaciones

    def verificar_estado(self):
        """
        Verifica el estado de todas las estaciones de cocina.
        """
        # print("Monitoreando cocina...") # Descomentar para debug
        for est in self._estaciones:
            
            if not est.verificar_equipamiento(): #
                print(f"ALERTA EQUIPAMIENTO: {est.get_nombre_estacion()} no operativo")

            if est.esta_saturada(): #
                print(f"ALERTA SATURACIÓN: {est.get_nombre_estacion()} está saturada")
            
            retrasadas = est.obtener_ordenes_retrasadas() #
            if retrasadas:
                print(f"ALERTA RETRASOS: {est.get_nombre_estacion()} tiene {len(retrasadas)} órdenes retrasadas")

            # Chequeos específicos por tipo de estación
            if isinstance(est, EstacionParrilla):
                if est.necesita_carbon(): #
                    print(f"ALERTA RECURSOS: {est.get_nombre_estacion()} necesita carbón")
            
            elif isinstance(est, EstacionBebidas):
                if est.necesita_hielo(): #
                    print(f"ALERTA RECURSOS: {est.get_nombre_estacion()} necesita hielo")
                if est.necesita_cristaleria(): #
                    print(f"ALERTA RECURSOS: {est.get_nombre_estacion()} necesita cristalería")
            
            elif isinstance(est, EstacionPastas):
                if est.necesita_pasta(): #
                    print(f"ALERTA RECURSOS: {est.get_nombre_estacion()} necesita pasta")

# ================================================================================
# ARCHIVO 4/4: monitor_inventario_task.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/control/monitor_inventario_task.py
# ================================================================================

from typing import List
from src.monitoreo.control.monitor_base_task import MonitorBase
from src.entidades.inventario.ingrediente import Ingrediente
from src.entidades.inventario.alerta_stock import AlertaStock, TipoAlerta
# Asumimos que tienes un gestor que maneja las alertas
# from src.gestores.gestor_alertas import GestorDeAlertas 

class MonitorInventario(MonitorBase):
    
    def __init__(self, ingredientes: List[Ingrediente], intervalo_segundos: float):
        super().__init__(intervalo_segundos)
        self._ingredientes = ingredientes
        # self._gestor_alertas = GestorDeAlertas() # O se recibe por parámetro

    def verificar_estado(self):
        """
        Verifica el estado de todos los ingredientes y genera alertas.
        """
        # print("Monitoreando inventario...") # Descomentar para debug
        for ing in self._ingredientes:
            
            if ing.esta_vencido(): #
                # Lógica para generar una alerta de vencimiento
                # self._gestor_alertas.crear_alerta(ing, TipoAlerta.VENCIDO, ...)
                print(f"ALERTA VENCIDO: {ing.get_nombre()}")
                
            elif ing.esta_por_vencer(): #
                # Lógica para alerta "por vencer"
                print(f"ALERTA POR VENCER: {ing.get_nombre()}")

            if ing.esta_agotado(): #
                print(f"ALERTA AGOTADO: {ing.get_nombre()}")
            
            elif ing.esta_en_stock_critico(): #
                print(f"ALERTA STOCK CRITICO: {ing.get_nombre()}")

            elif ing.necesita_reabastecimiento(): #
                print(f"ALERTA STOCK BAJO: {ing.get_nombre()}")

