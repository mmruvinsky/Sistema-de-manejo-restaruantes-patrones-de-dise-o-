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
