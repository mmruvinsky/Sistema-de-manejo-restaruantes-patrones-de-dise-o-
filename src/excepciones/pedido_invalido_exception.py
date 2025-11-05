from src.excepciones.restaurante_exception import RestauranteException

# ============= EXCEPCIONES DE PEDIDOS =============

class PedidoInvalidoException(RestauranteException):
    """Se lanza cuando un pedido es inválido"""
    
    def __init__(self, pedido_id: int, razon: str):
        mensaje = f"El pedido #{pedido_id} es inválido: {razon}"
        super().__init__(mensaje, "ERR_PEDIDO_INVALIDO")
        self.pedido_id = pedido_id
        self.razon = razon


class PedidoVacioException(RestauranteException):
    """Se lanza cuando se intenta procesar un pedido sin items"""
    
    def __init__(self, pedido_id: int):
        mensaje = f"El pedido #{pedido_id} no tiene items"
        super().__init__(mensaje, "ERR_PEDIDO_VACIO")
        self.pedido_id = pedido_id


class EstadoPedidoInvalidoException(RestauranteException):
    """Se lanza cuando se intenta realizar una operación con un estado inválido"""
    
    def __init__(self, pedido_id: int, estado_actual: str, estado_requerido: str):
        mensaje = (f"El pedido #{pedido_id} está en estado '{estado_actual}', "
                   f"se requiere estado '{estado_requerido}'")
        super().__init__(mensaje, "ERR_ESTADO_PEDIDO_INVALIDO")
        self.pedido_id = pedido_id
        self.estado_actual = estado_actual
        self.estado_requerido = estado_requerido


class ItemNoDisponibleException(RestauranteException):
    """Se lanza cuando un item del menú no está disponible"""
    
    def __init__(self, nombre_item: str):
        mensaje = f"El item '{nombre_item}' no está disponible en este momento"
        super().__init__(mensaje, "ERR_ITEM_NO_DISPONIBLE")
        self.nombre_item = nombre_item
