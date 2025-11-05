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