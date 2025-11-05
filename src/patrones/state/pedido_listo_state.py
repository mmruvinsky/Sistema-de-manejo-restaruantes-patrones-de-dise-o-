from src.patrones.state.pedido_state import IPedidoState
from src.patrones.state.pedido_servido_state import PedidoServidoState
from src.entidades.pedidos.estado_pedido import EstadoPedido
from src.entidades.pedidos.item_pedido import ItemPedido
from src.excepciones.pedido_invalido_exception import PedidoInvalidoException, EstadoPedidoInvalidoException

class PedidoListoState(IPedidoState):
    """
    Estado: Listo.
    Permite: servir.
    NO permite: agregar, cancelar, etc.
    """
    
    def agregar_item(self, item: ItemPedido):
        raise PedidoInvalidoException(
            self._pedido.get_id(), "No se pueden agregar items a un pedido listo"
        )
    
    def cancelar(self):
        raise PedidoInvalidoException(
            self._pedido.get_id(), "No se puede cancelar un pedido listo para servir"
        )
    
    def confirmar_preparacion(self):
        raise EstadoPedidoInvalidoException(
            self._pedido.get_id(), EstadoPedido.LISTO.value, EstadoPedido.EN_PREPARACION.value
        )

    def marcar_listo(self):
        print(f"Pedido {self._pedido.get_id()} ya está listo.")
        
    def servir(self):
        print(f"Pedido {self._pedido.get_id()} SERVIDO.")
        self._pedido.set_estado_interno(PedidoServidoState(self._pedido))