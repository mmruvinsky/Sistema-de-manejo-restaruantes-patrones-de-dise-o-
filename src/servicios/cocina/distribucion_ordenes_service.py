from src.entidades.pedidos.pedido import Pedido
from src.entidades.cocina.orden_cocina import OrdenCocina
from src.servicios.cocina.cocina_service import CocinaService

class DistribucionOrdenesService:
    """
    Servicio Singleton que toma un Pedido y lo divide en
    múltiples OrdenCocina, enviándolas al CocinaService.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._cocina_service = CocinaService()
        self._inicializado = True

    def distribuir_pedido(self, pedido: Pedido):
        """
        Toma un pedido, crea las órdenes de cocina y las distribuye.
        """
        if not pedido.get_items():
            print(f"Advertencia: Pedido #{pedido.get_id()} no tiene items para distribuir.")
            return

        print(f"Distribuyendo Pedido #{pedido.get_id()} en órdenes de cocina...")
        
        for item_pedido in pedido.get_items():
            # Crear una OrdenCocina para cada ItemPedido
            orden = OrdenCocina(
                item_pedido=item_pedido,
                pedido_id=pedido.get_id(),
                mesa_id=pedido.get_mesa_id()
            )
            
            # Usar el CocinaService para enviar la orden
            try:
                self._cocina_service.enviar_orden_a_estacion(orden)
            except ValueError as e:
                print(f"Error al distribuir orden: {e}")
                # Aquí se podría manejar la lógica de un item que no
                # tiene estación (ej. cancelar la orden)