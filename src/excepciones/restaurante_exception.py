
# ============= EXCEPCIONES BASE =============

class RestauranteException(Exception):
    """Excepción base para todas las excepciones del restaurante"""
    
    def __init__(self, mensaje: str, codigo_error: str = "ERR_GENERAL"):
        self.mensaje = mensaje
        self.codigo_error = codigo_error
        super().__init__(self.mensaje)
    
    def __str__(self):
        return f"[{self.codigo_error}] {self.mensaje}"
