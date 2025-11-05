from src.entidades.pedidos.pedido import Pedido
from src.patrones.decorator.precio_decorator import ICalculablePrecio
from src.patrones.decorator.descuento_decorator import DescuentoDecorator
from src.patrones.decorator.recargo_decorator import RecargoDecorator
from src.constantes import DESCUENTO_CLIENTE_FRECUENTE, RECARGO_DELIVERY
from src.entidades.pedidos.tipo_servicio import TipoServicio
from typing import Dict

class PedidoService:
    """
    Servicio Singleton para gestionar el CICLO DE VIDA de un Pedido
    y aplicar lógicas de negocio (como Decorators de precio).
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._pedidos_activos: Dict[int, Pedido] = {}
        self._inicializado = True
        print("Servicio de Pedidos inicializado.")
        
    def registrar_pedido(self, pedido: Pedido):
        self._pedidos_activos[pedido.get_id()] = pedido

    def get_pedido(self, pedido_id: int) -> Pedido:
        return self._pedidos_activos[pedido_id]

    # --- Métodos que delegan al PATRÓN STATE ---
    
    def confirmar_preparacion_pedido(self, pedido_id: int):
        pedido = self.get_pedido(pedido_id)
        pedido.get_estado().confirmar_preparacion()

    def marcar_pedido_listo(self, pedido_id: int):
        pedido = self.get_pedido(pedido_id)
        pedido.get_estado().marcar_listo()

    def servir_pedido(self, pedido_id: int):
        pedido = self.get_pedido(pedido_id)
        pedido.get_estado().servir()

    def cancelar_pedido(self, pedido_id: int):
        pedido = self.get_pedido(pedido_id)
        pedido.get_estado().cancelar()

    # --- Método que usa el PATRÓN DECORATOR ---

    def calcular_precio_final_con_cargos(self, pedido_id: int) -> float:
        """
        Calcula el precio final aplicando dinámicamente
        descuentos y recargos usando Decorators.
        """
        pedido = self.get_pedido(pedido_id)
        
        # 1. El componente base es el propio pedido
        componente_precio: ICalculablePrecio = pedido
        
        # 2. Envolver con decoradores según la lógica
        if pedido._es_cliente_frecuente:
            componente_precio = DescuentoDecorator(
                componente=componente_precio,
                porcentaje=DESCUENTO_CLIENTE_FRECUENTE
            )
            
        if pedido.get_tipo_servicio() == TipoServicio.DELIVERY:
            componente_precio = RecargoDecorator(
                componente=componente_precio,
                monto_fijo=RECARGO_DELIVERY
            )
        
        # (Se podrían agregar más, ej. Happy Hour, Recargo Servicio Mesa)
        
        # 3. El cálculo final es polimórfico
        precio_final = componente_precio.calcular_total()
        
        return precio_final