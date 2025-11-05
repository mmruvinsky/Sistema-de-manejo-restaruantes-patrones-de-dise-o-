"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/sensores
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/sensores/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: sensor_base_task.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/sensores/sensor_base_task.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/5: sensor_stock_task.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/sensores/sensor_stock_task.py
# ================================================================================

from src.patrones.observer import IObserver
from src.patrones.observer import IObservable
from src.entidades.inventario.ingrediente import Ingrediente
from src.entidades.inventario.alerta_stock import AlertaStock, TipoAlerta

class SensorStockObserver(IObserver):
    """
    Implementación del Patrón Observer. Escucha a los
    ingredientes (Observables).
    """
    def __init__(self):
        # self._gestor_alertas = GestorDeAlertas() # Idealmente
        pass

    def actualizar(self, observable: IObservable):
        if not isinstance(observable, Ingrediente):
            return

        # El 'observable' es el ingrediente que cambió
        ing = observable
        
        # print(f"DEBUG: SensorStockObserver notificado por {ing.get_nombre()}") # Debug
        
        if ing.esta_agotado():
            self.generar_alerta(ing, TipoAlerta.AGOTADO, "Stock en cero")
        elif ing.esta_en_stock_critico():
            msg = f"Stock crítico: {ing.get_cantidad_actual()} {ing.get_unidad_medida()}"
            self.generar_alerta(ing, TipoAlerta.STOCK_CRITICO, msg)
        elif ing.necesita_reabastecimiento():
            msg = f"Stock bajo: {ing.get_cantidad_actual()} {ing.get_unidad_medida()}"
            self.generar_alerta(ing, TipoAlerta.STOCK_BAJO, msg)
    
    def generar_alerta(self, ingrediente: Ingrediente, tipo: TipoAlerta, mensaje: str):
        alerta = AlertaStock(
            ingrediente_id=ingrediente.get_id(),
            ingrediente_nombre=ingrediente.get_nombre(),
            tipo_alerta=tipo,
            mensaje=mensaje
        )
        print("\n--- 🚨 ALERTA DE STOCK (OBSERVER) 🚨 ---")
        print(str(alerta))
        print("---------------------------------------\n")

# ================================================================================
# ARCHIVO 4/5: sensor_temperatura_cocina_task.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/sensores/sensor_temperatura_cocina_task.py
# ================================================================================

import random
from typing import List
from src.monitoreo.sensores.sensor_base_task import SensorBase #
from src.entidades.cocina.estacion_cocina import EstacionCocina #
from src.constantes import TEMPERATURA_COCINA_MIN, TEMPERATURA_COCINA_MAX #

class SensorTemperatura(SensorBase):
    
    def __init__(self, estaciones: List[EstacionCocina], intervalo_segundos: float):
        super().__init__(intervalo_segundos)
        self._estaciones = estaciones

    def tomar_lectura(self):
        """
        Simula una lectura de temperatura y la actualiza
        en la estación de cocina correspondiente.
        """
        for estacion in self._estaciones:
            if not estacion.esta_activa(): #
                continue
            
            # Simular una fluctuación de temperatura
            temp_actual = estacion.get_temperatura_actual() #
            fluctuacion = random.uniform(-0.5, 0.5)
            
            # (No aplica fluctuación a estaciones especiales como parrilla o postres 
            # que fijan su propia temp, solo a la temp. ambiente de la estación)
            if temp_actual >= TEMPERATURA_COCINA_MIN and temp_actual <= TEMPERATURA_COCINA_MAX: #
                nueva_temp = max(TEMPERATURA_COCINA_MIN, min(TEMPERATURA_COCINA_MAX, temp_actual + fluctuacion))
                estacion.set_temperatura_actual(nueva_temp) #

# ================================================================================
# ARCHIVO 5/5: sensor_tiempo_de_espera_task.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/monitoreo/sensores/sensor_tiempo_de_espera_task.py
# ================================================================================

from typing import List
from src.monitoreo.sensores.sensor_base_task import SensorBase #
from src.entidades.cocina.estacion_cocina import EstacionCocina #

class SensorTiempoEspera(SensorBase):
    
    def __init__(self, estaciones: List[EstacionCocina], intervalo_segundos: float):
        super().__init__(intervalo_segundos)
        self._estaciones = estaciones
        # self._gestor_alertas = GestorDeAlertas() # O se recibe por parámetro

    def tomar_lectura(self):
        """
        Verifica todas las órdenes en preparación y busca retrasos.
        """
        # print("Sensor de tiempo verificando...") # Descomentar para debug
        
        for estacion in self._estaciones:
            if not estacion.esta_activa(): #
                continue
                
            ordenes_retrasadas = estacion.obtener_ordenes_retrasadas() #
            
            for orden in ordenes_retrasadas:
                # Generar una alerta para esta orden
                # (Aquí también usarías tu GestorDeAlertas)
                
                # Simulación con print:
                tiempo_espera = orden.calcular_tiempo_espera_actual() #
                print(f"\n--- SENSOR DE TIEMPO ---")
                print(f"ALERTA RETRASO: Orden #{orden.get_id()} en {estacion.get_nombre_estacion()}") #
                print(f"  Tiempo actual: {tiempo_espera} min (Estimado: {orden.get_tiempo_estimado()} min)") #
                print("--------------------------\n")

