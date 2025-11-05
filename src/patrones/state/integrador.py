"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/state
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 7
"""

# ================================================================================
# ARCHIVO 1/7: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/state/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/7: pedido_cancelado_state.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/state/pedido_cancelado_state.py
# ================================================================================

from src.patrones.state.pedido_state import IPedidoState
from src.entidades.pedidos.item_pedido import ItemPedido
from src.excepciones.pedido_invalido_exception import PedidoInvalidoException

class PedidoCanceladoState(IPedidoState):
    """
    Estado: Cancelado (Final).
    No permite más acciones.
    """
    
    def _error(self):
        raise PedidoInvalidoException(
            self._pedido.get_id(), "El pedido está cancelado y no admite cambios."
        )

    def agregar_item(self, item: ItemPedido):
        self._error()
    
    def cancelar(self):
        print(f"Pedido {self._pedido.get_id()} ya está cancelado.")
    
    def confirmar_preparacion(self):
        self._error()

    def marcar_listo(self):
        self._error()
        
    def servir(self):
        self._error()

# ================================================================================
# ARCHIVO 3/7: pedido_en_preparacion_state.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/state/pedido_en_preparacion_state.py
# ================================================================================

from src.patrones.state.pedido_state import IPedidoState
from src.patrones.state.pedido_listo_state import PedidoListoState
from src.patrones.state.pedido_cancelado_state import PedidoCanceladoState
from src.entidades.pedidos.estado_pedido import EstadoPedido
from src.entidades.pedidos.item_pedido import ItemPedido
from src.excepciones.pedido_invalido_exception import PedidoInvalidoException, EstadoPedidoInvalidoException

class PedidoEnPreparacionState(IPedidoState):
    """
    Estado: En Preparación.
    Permite: cancelar o marcar como listo.
    NO permite: agregar items.
    """
    
    def agregar_item(self, item: ItemPedido):
        raise PedidoInvalidoException(
            self._pedido.get_id(), "No se pueden agregar items a un pedido en preparación"
        )
    
    def cancelar(self):
        print(f"Pedido {self._pedido.get_id()} CANCELADO (en preparación).")
        self._pedido.set_estado_interno(PedidoCanceladoState(self._pedido))
    
    def confirmar_preparacion(self):
        # Ya está en este estado, no hacer nada o lanzar error leve
        print(f"Pedido {self._pedido.get_id()} ya está en preparación.")

    def marcar_listo(self):
        print(f"Pedido {self._pedido.get_id()} está LISTO.")
        self._pedido.set_estado_interno(PedidoListoState(self._pedido))
        
    def servir(self):
        raise EstadoPedidoInvalidoException(
            self._pedido.get_id(), EstadoPedido.EN_PREPARACION.value, EstadoPedido.SERVIDO.value
        )

# ================================================================================
# ARCHIVO 4/7: pedido_listo_state.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/state/pedido_listo_state.py
# ================================================================================

from src.patrones.state.pedido_state import IPedidoState
from src.patrones.state.pedido_servido_state import PedidoServidoState
from src.entidades.pedidos.estado_pedido import EstadoPedido
from src.entidades.pedidos.item_pedido import ItemPedido
from src.excepciones.pedido_invalido_exception import PedidoInvalidoException, EstadoPedidoInvalidoException

class PedidoListoState(IPedidoState):
    """
    Estado: Listo.
    Permite: servir.
    NO permite: agregar, cancelar, etc.
    """
    
    def agregar_item(self, item: ItemPedido):
        raise PedidoInvalidoException(
            self._pedido.get_id(), "No se pueden agregar items a un pedido listo"
        )
    
    def cancelar(self):
        raise PedidoInvalidoException(
            self._pedido.get_id(), "No se puede cancelar un pedido listo para servir"
        )
    
    def confirmar_preparacion(self):
        raise EstadoPedidoInvalidoException(
            self._pedido.get_id(), EstadoPedido.LISTO.value, EstadoPedido.EN_PREPARACION.value
        )

    def marcar_listo(self):
        print(f"Pedido {self._pedido.get_id()} ya está listo.")
        
    def servir(self):
        print(f"Pedido {self._pedido.get_id()} SERVIDO.")
        self._pedido.set_estado_interno(PedidoServidoState(self._pedido))

# ================================================================================
# ARCHIVO 5/7: pedido_recibidio_state.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/state/pedido_recibidio_state.py
# ================================================================================

from src.patrones.state.pedido_state import IPedidoState
from src.patrones.state.pedido_en_preparacion_state import PedidoEnPreparacionState
from src.patrones.state.pedido_cancelado_state import PedidoCanceladoState
from src.entidades.pedidos.estado_pedido import EstadoPedido
from src.entidades.pedidos.item_pedido import ItemPedido
from src.excepciones.pedido_invalido_exception import EstadoPedidoInvalidoException

class PedidoRecibidoState(IPedidoState):
    """
    Estado: Pedido Recibido.
    Permite: agregar items, cancelar, o pasar a preparación.
    """
    
    def agregar_item(self, item: ItemPedido):
        # En estado RECIBIDO, sí se pueden agregar items
        self._pedido._items.append(item)
    
    def cancelar(self):
        print(f"Pedido {self._pedido.get_id()} CANCELADO.")
        self._pedido.set_estado_interno(PedidoCanceladoState(self._pedido))
    
    def confirmar_preparacion(self):
        print(f"Pedido {self._pedido.get_id()} pasa a EN PREPARACIÓN.")
        self._pedido.set_estado_interno(PedidoEnPreparacionState(self._pedido))

    def marcar_listo(self):
        raise EstadoPedidoInvalidoException(
            self._pedido.get_id(), EstadoPedido.RECIBIDO.value, EstadoPedido.LISTO.value
        )
        
    def servir(self):
        raise EstadoPedidoInvalidoException(
            self._pedido.get_id(), EstadoPedido.RECIBIDO.value, EstadoPedido.SERVIDO.value
        )

# ================================================================================
# ARCHIVO 6/7: pedido_servido_state.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/state/pedido_servido_state.py
# ================================================================================

from src.patrones.state.pedido_state import IPedidoState
from src.entidades.pedidos.item_pedido import ItemPedido
from src.excepciones.pedido_invalido_exception import PedidoInvalidoException

class PedidoServidoState(IPedidoState):
    """
    Estado: Servido (Final).
    No permite más acciones.
    """
    
    def _error(self):
        raise PedidoInvalidoException(
            self._pedido.get_id(), "El pedido ya fue servido y no admite más cambios."
        )

    def agregar_item(self, item: ItemPedido):
        self._error()
    
    def cancelar(self):
        self._error()
    
    def confirmar_preparacion(self):
        self._error()

    def marcar_listo(self):
        self._error()
        
    def servir(self):
        print(f"Pedido {self._pedido.get_id()} ya fue servido.")

# ================================================================================
# ARCHIVO 7/7: pedido_state.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/state/pedido_state.py
# ================================================================================

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

