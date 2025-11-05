from src.patrones.strategy.metodo_coccion_strategy import IMetodoCoccionStrategy
from src.entidades.cocina.orden_cocina import OrdenCocina

class CoccionParrillaStrategy(IMetodoCoccionStrategy):
    """
    Estrategia concreta para cocinar a la parrilla.
    """
    def ejecutar_coccion(self, orden: OrdenCocina) -> str:
        item = orden.get_item_pedido().get_item_menu().get_nombre()
        # Aquí podría ir lógica más compleja, como verificar
        # el punto de cocción de la orden.
        mensaje = f"🔥 {item} cocinado a la Parrilla."
        orden.agregar_nota_chef(mensaje)
        return mensaje