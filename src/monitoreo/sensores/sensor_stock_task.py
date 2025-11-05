from typing import List
from src.monitoreo.sensores.sensor_base_task import SensorBase #
from src.entidades.inventario.ingrediente import Ingrediente #
from src.entidades.inventario.alerta_stock import AlertaStock, TipoAlerta #
# from src.gestores.gestor_alertas import GestorDeAlertas # Necesitarás un gestor central

class SensorStock(SensorBase):
    
    def __init__(self, ingredientes: List[Ingrediente], intervalo_segundos: float):
        super().__init__(intervalo_segundos)
        self._ingredientes = ingredientes
        # self._gestor_alertas = GestorDeAlertas() # O se recibe por parámetro

    def tomar_lectura(self):
        """
        Verifica el estado de todos los ingredientes y genera alertas.
        """
        # print("Sensor de stock verificando...") # Descomentar para debug
        for ing in self._ingredientes:
            
            # NOTA: Aquí se generan las alertas. Necesitarás un 
            # GestorDeAlertas para centralizar y mostrarlas.
            # Por ahora, usamos print().

            if ing.esta_vencido(): #
                self.generar_alerta(ing, TipoAlerta.VENCIDO, "El ingrediente está vencido")
                
            elif ing.esta_por_vencer(): #
                msg = f"Vence en {ing.dias_hasta_vencimiento()} días" #
                self.generar_alerta(ing, TipoAlerta.POR_VENCER, msg)

            if ing.esta_agotado(): #
                self.generar_alerta(ing, TipoAlerta.AGOTADO, "Stock en cero")
            
            elif ing.esta_en_stock_critico(): #
                msg = f"Stock crítico: {ing.get_cantidad_actual()} {ing.get_unidad_medida()}" #
                self.generar_alerta(ing, TipoAlerta.STOCK_CRITICO, msg)

            elif ing.necesita_reabastecimiento(): #
                msg = f"Stock bajo: {ing.get_cantidad_actual()} {ing.get_unidad_medida()}" #
                self.generar_alerta(ing, TipoAlerta.STOCK_BAJO, msg)
    
    def generar_alerta(self, ingrediente: Ingrediente, tipo: TipoAlerta, mensaje: str):
        """
        Crea un objeto AlertaStock y lo envía a un gestor central.
        (Simulado con print por ahora)
        """
        alerta = AlertaStock(
            ingrediente_id=ingrediente.get_id(), #
            ingrediente_nombre=ingrediente.get_nombre(), #
            tipo_alerta=tipo,
            mensaje=mensaje
        )
        
        # Aquí llamarías a tu gestor:
        # self._gestor_alertas.registrar_alerta(alerta)
        
        # Simulación:
        print(f"\n--- SENSOR DE STOCK ---")
        print(str(alerta))
        print("-----------------------\n")