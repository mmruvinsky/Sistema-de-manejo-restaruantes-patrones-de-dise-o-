from src.patrones.state.pedido_state import IPedidoState
from src.patrones.state.pedido_listo_state import PedidoListoState
from src.patrones.state.pedido_cancelado_state import PedidoCanceladoState
from src.entidades.pedidos.estado_pedido import EstadoPedido
from src.entidades.pedidos.item_pedido import ItemPedido
from src.excepciones.pedido_invalido_exception import PedidoInvalidoException, EstadoPedidoInvalidoException

class PedidoEnPreparacionState(IPedidoState):
    """
    Estado: En Preparación.
    Permite: cancelar o marcar como listo.
    NO permite: agregar items.
    """
    
    def agregar_item(self, item: ItemPedido):
        raise PedidoInvalidoException(
            self._pedido.get_id(), "No se pueden agregar items a un pedido en preparación"
        )
    
    def cancelar(self):
        print(f"Pedido {self._pedido.get_id()} CANCELADO (en preparación).")
        self._pedido.set_estado_interno(PedidoCanceladoState(self._pedido))
    
    def confirmar_preparacion(self):
        # Ya está en este estado, no hacer nada o lanzar error leve
        print(f"Pedido {self._pedido.get_id()} ya está en preparación.")

    def marcar_listo(self):
        print(f"Pedido {self._pedido.get_id()} está LISTO.")
        self._pedido.set_estado_interno(PedidoListoState(self._pedido))
        
    def servir(self):
        raise EstadoPedidoInvalidoException(
            self._pedido.get_id(), EstadoPedido.EN_PREPARACION.value, EstadoPedido.SERVIDO.value
        )