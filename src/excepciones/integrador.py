"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/excepciones
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/excepciones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: ingrediente_agotado_exception.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/excepciones/ingrediente_agotado_exception.py
# ================================================================================

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



# ================================================================================
# ARCHIVO 3/6: mesa_ocupada_exception.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/excepciones/mesa_ocupada_exception.py
# ================================================================================



# ================================================================================
# ARCHIVO 4/6: pedido_invalido_exception.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/excepciones/pedido_invalido_exception.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/excepciones/persistencia_exception.py
# ================================================================================

from src.excepciones.restaurante_exception import RestauranteException

# ============= EXCEPCIONES DE PERSISTENCIA =============

class PersistenciaException(RestauranteException):
    """Se lanza cuando hay un error en la persistencia de datos"""
    
    def __init__(self, operacion: str, detalle: str):
        mensaje = f"Error en operación de persistencia '{operacion}': {detalle}"
        super().__init__(mensaje, "ERR_PERSISTENCIA")
        self.operacion = operacion
        self.detalle = detalle


class ArchivoNoEncontradoException(PersistenciaException):
    """Se lanza cuando no se encuentra un archivo"""
    
    def __init__(self, ruta_archivo: str):
        super().__init__("lectura", f"No se encontró el archivo: {ruta_archivo}")
        self.ruta_archivo = ruta_archivo


class ErrorSerializacionException(PersistenciaException):
    """Se lanza cuando hay un error al serializar/deserializar datos"""
    
    def __init__(self, tipo_dato: str, detalle: str):
        super().__init__("serialización", f"Error al serializar '{tipo_dato}': {detalle}")
        self.tipo_dato = tipo_dato


# ================================================================================
# ARCHIVO 6/6: restaurante_exception.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/excepciones/restaurante_exception.py
# ================================================================================


# ============= EXCEPCIONES BASE =============

class RestauranteException(Exception):
    """Excepción base para todas las excepciones del restaurante"""
    
    def __init__(self, mensaje: str, codigo_error: str = "ERR_GENERAL"):
        self.mensaje = mensaje
        self.codigo_error = codigo_error
        super().__init__(self.mensaje)
    
    def __str__(self):
        return f"[{self.codigo_error}] {self.mensaje}"


