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