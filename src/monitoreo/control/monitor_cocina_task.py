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