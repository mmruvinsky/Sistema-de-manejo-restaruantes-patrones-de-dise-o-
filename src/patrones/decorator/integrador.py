"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/decorator
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/decorator/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: descuento_decorator.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/decorator/descuento_decorator.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: precio_decorator.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/decorator/precio_decorator.py
# ================================================================================

from abc import ABC, abstractmethod

class ICalculablePrecio(ABC):
    """
    Interfaz Componente: Define la operación que será decorada.
    Tu clase 'Pedido' implementará esta interfaz.
    """
    @abstractmethod
    def calcular_subtotal(self) -> float:
        pass
        
    @abstractmethod
    def calcular_total(self) -> float:
        pass

class PrecioDecoratorBase(ICalculablePrecio):
    """
    Clase Decorador Abstracta.
    Mantiene una referencia al componente que envuelve.
    """
    def __init__(self, componente: ICalculablePrecio):
        self._componente = componente
    
    @property
    def componente(self) -> ICalculablePrecio:
        return self._componente
        
    def calcular_subtotal(self) -> float:
        # Delega al componente envuelto
        return self._componente.calcular_subtotal()

    @abstractmethod
    def calcular_total(self) -> float:
        # Delega al componente envuelto (las subclases lo modificarán)
        pass

# ================================================================================
# ARCHIVO 4/4: recargo_decorator.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/patrones/decorator/recargo_decorator.py
# ================================================================================

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

