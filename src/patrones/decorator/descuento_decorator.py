from src.patrones.decorator.precio_decorator import PrecioDecoratorBase, ICalculablePrecio

class DescuentoDecorator(PrecioDecoratorBase):
    """
    Decorador concreto: Aplica un descuento porcentual.
    """
    def __init__(self, componente: ICalculablePrecio, porcentaje: float):
        super().__init__(componente)
        self._porcentaje_descuento = porcentaje # Ej: 10 para 10%
        
    def calcular_total(self) -> float:
        # 1. Obtiene el total del componente envuelto
        precio_base = self._componente.calcular_total()
        
        # 2. Calcula el descuento sobre el subtotal
        #    (Importante: usar subtotal para no descontar sobre otros decoradores)
        subtotal = self.calcular_subtotal()
        descuento = subtotal * (self._porcentaje_descuento / 100.0)
        
        # 3. Aplica su propia lógica
        return precio_base - descuento