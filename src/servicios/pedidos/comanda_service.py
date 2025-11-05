from typing import Optional
from src.entidades.pedidos.pedido import Pedido
from src.entidades.pedidos.item_pedido import ItemPedido
from src.entidades.pedidos.tipo_servicio import TipoServicio

# --- Implementación del Patrón Builder ---
# (Lo ponemos aquí ya que no tienes una carpeta 'builder')

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