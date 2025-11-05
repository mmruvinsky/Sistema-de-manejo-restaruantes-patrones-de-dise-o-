from src.patrones.state.pedido_state import IPedidoState
from src.patrones.state.pedido_en_preparacion_state import PedidoEnPreparacionState
from src.patrones.state.pedido_cancelado_state import PedidoCanceladoState
from src.entidades.pedidos.estado_pedido import EstadoPedido
from src.entidades.pedidos.item_pedido import ItemPedido
from src.excepciones.pedido_invalido_exception import EstadoPedidoInvalidoException

class PedidoRecibidoState(IPedidoState):
    """
    Estado: Pedido Recibido.
    Permite: agregar items, cancelar, o pasar a preparación.
    """
    
    def agregar_item(self, item: ItemPedido):
        # En estado RECIBIDO, sí se pueden agregar items
        self._pedido._items.append(item)
    
    def cancelar(self):
        print(f"Pedido {self._pedido.get_id()} CANCELADO.")
        self._pedido.set_estado_interno(PedidoCanceladoState(self._pedido))
    
    def confirmar_preparacion(self):
        print(f"Pedido {self._pedido.get_id()} pasa a EN PREPARACIÓN.")
        self._pedido.set_estado_interno(PedidoEnPreparacionState(self._pedido))

    def marcar_listo(self):
        raise EstadoPedidoInvalidoException(
            self._pedido.get_id(), EstadoPedido.RECIBIDO.value, EstadoPedido.LISTO.value
        )
        
    def servir(self):
        raise EstadoPedidoInvalidoException(
            self._pedido.get_id(), EstadoPedido.RECIBIDO.value, EstadoPedido.SERVIDO.value
        )