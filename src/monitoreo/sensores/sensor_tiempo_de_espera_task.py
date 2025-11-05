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