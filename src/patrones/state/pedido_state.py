from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# Importación circular: Pedido necesita Estado, Estado necesita Pedido
if TYPE_CHECKING:
    from src.entidades.pedidos.pedido import Pedido
    from src.entidades.pedidos.item_pedido import ItemPedido

class IPedidoState(ABC):
    """
    Interfaz (Patrón State) para los estados del Pedido.
    Define las operaciones que pueden variar según el estado.
    """
    
    def __init__(self, pedido: Pedido):
        self._pedido = pedido

    @abstractmethod
    def agregar_item(self, item: ItemPedido):
        """Intenta agregar un item al pedido"""
        pass

    @abstractmethod
    def cancelar(self):
        """Intenta cancelar el pedido"""
        pass
    
    @abstractmethod
    def confirmar_preparacion(self):
        """Intenta pasar el pedido a preparación"""
        pass
        
    @abstractmethod
    def marcar_listo(self):
        """Intenta marcar el pedido como listo para servir"""
        pass
        
    @abstractmethod
    def servir(self):
        """Intenta servir el pedido"""
        pass
        
    def __str__(self) -> str:
        return self.__class__.__name__