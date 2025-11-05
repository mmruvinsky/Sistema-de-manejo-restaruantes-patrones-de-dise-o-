from src.excepciones.restaurante_exception import RestauranteException

# ============= EXCEPCIONES DE INGREDIENTES =============

class IngredienteAgotadoException(RestauranteException):
    """Se lanza cuando un ingrediente está agotado"""
    
    def __init__(self, nombre_ingrediente: str, cantidad_requerida: float = 0):
        mensaje = f"El ingrediente '{nombre_ingrediente}' está agotado"
        if cantidad_requerida > 0:
            mensaje += f" (se requieren {cantidad_requerida} unidades)"
        super().__init__(mensaje, "ERR_INGREDIENTE_AGOTADO")
        self.nombre_ingrediente = nombre_ingrediente
        self.cantidad_requerida = cantidad_requerida


class IngredienteVencidoException(RestauranteException):
    """Se lanza cuando se intenta usar un ingrediente vencido"""
    
    def __init__(self, nombre_ingrediente: str, fecha_vencimiento):
        mensaje = f"El ingrediente '{nombre_ingrediente}' está vencido (venció el {fecha_vencimiento})"
        super().__init__(mensaje, "ERR_INGREDIENTE_VENCIDO")
        self.nombre_ingrediente = nombre_ingrediente
        self.fecha_vencimiento = fecha_vencimiento


class StockInsuficienteException(RestauranteException):
    """Se lanza cuando no hay suficiente stock de un ingrediente"""
    
    def __init__(self, nombre_ingrediente: str, cantidad_disponible: float, cantidad_requerida: float):
        mensaje = (f"Stock insuficiente de '{nombre_ingrediente}'. "
                   f"Disponible: {cantidad_disponible}, Requerido: {cantidad_requerida}")
        super().__init__(mensaje, "ERR_STOCK_INSUFICIENTE")
        self.nombre_ingrediente = nombre_ingrediente
        self.cantidad_disponible = cantidad_disponible
        self.cantidad_requerida = cantidad_requerida

