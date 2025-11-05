from src.patrones.observer.observer import IObserver
from src.patrones.observer.observable import IObservable
from src.entidades.cocina.orden_cocina import OrdenCocina
from src.entidades.cocina.estado_orden import EstadoOrden

class ControlCalidadService(IObserver):
    """
    Servicio Singleton que actúa como Observador.
    Puede "observar" órdenes de cocina y reaccionar cuando
    pasan al estado LISTA para verificar la calidad.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._inicializado = True
        print("Servicio de Control de Calidad inicializado.")

    def actualizar(self, observable: IObservable):
        """
        Método de IObserver. Se activa cuando un observable
        (ej. una OrdenCocina) notifica un cambio.
        """
        if not isinstance(observable, OrdenCocina):
            return
            
        orden = observable
        
        # Si la orden está LISTA, simular una verificación
        if orden.get_estado() == EstadoOrden.LISTA:
            self.verificar_orden(orden)
            
    def verificar_orden(self, orden: OrdenCocina):
        """
        Simula la lógica de control de calidad.
        """
        # Lógica de QC: ¿El plato cumple los estándares?
        # ¿Tiene las observaciones correctas?
        print(f"QC: Verificando Orden #{orden.get_id()}...")
        
        # Simulación de falla
        if "extra" in orden.get_observaciones_cliente().lower() and "extra" not in orden.get_notas_chef().lower():
             print(f"QC FALLIDO: Orden #{orden.get_id()} no tiene las notas de 'extra' aplicadas.")
             # Aquí se podría devolver la orden a EN_PREPARACION
        else:
             print(f"QC APROBADO: Orden #{orden.get_id()} lista para entregar.")