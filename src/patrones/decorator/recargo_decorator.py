from src.patrones.decorator.precio_decorator import PrecioDecoratorBase, ICalculablePrecio

class RecargoDecorator(PrecioDecoratorBase):
    """
    Decorador concreto: Aplica un recargo fijo (ej. Delivery).
    """
    def __init__(self, componente: ICalculablePrecio, monto_fijo: float):
        super().__init__(componente)
        self._monto_recargo = monto_fijo
        
    def calcular_total(self) -> float:
        # 1. Obtiene el total del componente envuelto
        precio_base = self._componente.calcular_total()
        
        # 2. Aplica su propia lógica
        return precio_base + self._monto_recargo