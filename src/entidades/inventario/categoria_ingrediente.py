from enum import Enum

class CategoriaIngrediente(Enum):
    """Categorías de ingredientes para el inventario"""
    CARNES = "Carnes"
    PESCADOS_MARISCOS = "Pescados y Mariscos"
    VERDURAS = "Verduras"
    FRUTAS = "Frutas"
    LACTEOS = "Lácteos"
    CEREALES_GRANOS = "Cereales y Granos"
    ESPECIAS_CONDIMENTOS = "Especias y Condimentos"
    ACEITES_SALSAS = "Aceites y Salsas"
    BEBIDAS = "Bebidas"
    PANADERIA = "Panadería"
    POSTRES_DULCES = "Postres y Dulces"
    OTROS = "Otros"
    
    def __str__(self):
        return self.value
    
    @classmethod
    def obtener_categorias(cls):
        """Retorna lista de todas las categorías"""
        return [cat.value for cat in cls]