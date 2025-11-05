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