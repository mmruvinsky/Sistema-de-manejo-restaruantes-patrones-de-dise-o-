"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/pedidos
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/pedidos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: comanda_service.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/pedidos/comanda_service.py
# ================================================================================

from typing import Optional
from src.entidades.pedidos.pedido import Pedido
from src.entidades.pedidos.item_pedido import ItemPedido
from src.entidades.pedidos.tipo_servicio import TipoServicio


class PedidoBuilder:
    """
    Patrón Builder para construir un objeto Pedido complejo
    paso a paso.
    """
    def __init__(self, cliente_id: int):
        self._cliente_id = cliente_id
        self._mesa_id: Optional[int] = None
        self._tipo_servicio: TipoServicio = TipoServicio.EN_SALON
        self._items: List[ItemPedido] = []
        self._mozo_id: Optional[int] = None
        self._observaciones: str = ""
        self._es_happy_hour: bool = False
        self._es_frecuente: bool = False
    
    def para_mesa(self, mesa_id: int):
        self._mesa_id = mesa_id
        self._tipo_servicio = TipoServicio.EN_SALON
        return self
        
    def para_delivery(self, direccion: str):
        self._mesa_id = None
        self._tipo_servicio = TipoServicio.DELIVERY
        self.con_observacion(f"Enviar a: {direccion}")
        return self
        
    def con_mozo(self, mozo_id: int):
        self._mozo_id = mozo_id
        return self
        
    def con_item(self, item: ItemPedido):
        self._items.append(item)
        return self
        
    def con_observacion(self, observacion: str):
        self._observaciones = observacion
        return self

    def construir(self) -> Pedido:
        if not self._items:
            raise ValueError("No se puede construir un pedido sin items")
        
        pedido = Pedido(
            cliente_id=self._cliente_id,
            mesa_id=self._mesa_id,
            tipo_servicio=self._tipo_servicio
        )
        
        for item in self._items:
            # Usamos el método delegado al Estado
            pedido.agregar_item(item) 
            
        if self._mozo_id:
            pedido.set_mozo_id(self._mozo_id)
            
        pedido.set_observaciones(self._observaciones)
        
        # (Aquí se podrían setear también _es_happy_hour, etc.)
        
        return pedido

# --- Servicio Comanda ---

class ComandaService:
    """
    Servicio Singleton para la TOMA de pedidos.
    Su principal función es exponer el PedidoBuilder.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._inicializado = True
        print("Servicio de Comandas inicializado.")

    def iniciar_nuevo_pedido(self, cliente_id: int) -> PedidoBuilder:
        """
        Retorna un Builder para construir un nuevo pedido.
        """
        print(f"Iniciando nuevo pedido para cliente {cliente_id}...")
        return PedidoBuilder(cliente_id)

    def finalizar_pedido(self, builder: PedidoBuilder) -> Pedido:
        """
        Construye el pedido desde el builder.
        Aquí se podría registrar en PedidoService.
        """
        pedido = builder.construir()
        print(f"Pedido #{pedido.get_id()} creado y listo para preparación.")
        return pedido

# ================================================================================
# ARCHIVO 3/3: pedido_service.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/pedidos/pedido_service.py
# ================================================================================

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

