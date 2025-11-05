from src.patrones.state.pedido_state import IPedidoState
from src.entidades.pedidos.item_pedido import ItemPedido
from src.excepciones.pedido_invalido_exception import PedidoInvalidoException

class PedidoServidoState(IPedidoState):
    """
    Estado: Servido (Final).
    No permite más acciones.
    """
    
    def _error(self):
        raise PedidoInvalidoException(
            self._pedido.get_id(), "El pedido ya fue servido y no admite más cambios."
        )

    def agregar_item(self, item: ItemPedido):
        self._error()
    
    def cancelar(self):
        self._error()
    
    def confirmar_preparacion(self):
        self._error()

    def marcar_listo(self):
        self._error()
        
    def servir(self):
        print(f"Pedido {self._pedido.get_id()} ya fue servido.")