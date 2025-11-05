from src.patrones.strategy.metodo_coccion_strategy import IMetodoCoccionStrategy
from src.entidades.cocina.orden_cocina import OrdenCocina

class CoccionVaporStrategy(IMetodoCoccionStrategy):
    """
    Estrategia concreta para cocinar al vapor.
    """
    def ejecutar_coccion(self, orden: OrdenCocina) -> str:
        item = orden.get_item_pedido().get_item_menu().get_nombre()
        mensaje = f"💨 {item} cocinado al Vapor."
        orden.agregar_nota_chef(mensaje)
        return mensaje