"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/cocina
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/cocina/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: cocina_service.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/cocina/cocina_service.py
# ================================================================================

# src/servicios/cocina/cocina_service.py

from typing import List, Dict, Optional
from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.entidades.cocina.orden_cocina import OrdenCocina
from src.patrones.factory.estacion_factory import EstacionFactory

class CocinaService:
    """
    Servicio Singleton que gestiona todas las estaciones de cocina.
    Utiliza el EstacionFactory para crear las estaciones.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Evita la re-inicialización
        if hasattr(self, '_inicializado'):
            return
        
        self._estaciones: Dict[str, EstacionCocina] = {}
        self._inicializar_estaciones_std()
        self._inicializado = True
        
    def _inicializar_estaciones_std(self):
        """Crea las estaciones de cocina estándar al inicio."""
        
        # --- LÍNEA CORREGIDA ---
        # Eliminamos "Plancha" de la lista
        nombres_estaciones = ["Parrilla", "Pastas", "Postres", "Bebidas", "Cocina"]
        
        for nombre in nombres_estaciones:
            try:
                estacion = EstacionFactory.crear_estacion(nombre)
                self.registrar_estacion(estacion)
            except ValueError as e:
                print(f"Advertencia: No se pudo crear la estación {nombre}: {e}")

    def registrar_estacion(self, estacion: EstacionCocina):
        nombre = estacion.get_nombre_estacion()
        if nombre not in self._estaciones:
            self._estaciones[nombre] = estacion
            print(f"Estación registrada: {nombre}")
        
    def get_estacion(self, nombre: str) -> Optional[EstacionCocina]:
        return self._estaciones.get(nombre)

    def get_todas_las_estaciones(self) -> List[EstacionCocina]:
        return list(self._estaciones.values())

    def enviar_orden_a_estacion(self, orden: OrdenCocina):
        """
        Envía una OrdenCocina a su estación correspondiente.
        """
        nombre_estacion = orden.get_estacion_asignada()
        estacion = self.get_estacion(nombre_estacion)
        
        if not estacion:
            # Esta excepción ahora se lanzará si un item devuelve "Plancha"
            raise ValueError(f"No se encontró la estación '{nombre_estacion}' para la orden #{orden.get_id()}")
            
        estacion.recibir_orden(orden)
        print(f"Orden #{orden.get_id()} enviada a {nombre_estacion}")

# ================================================================================
# ARCHIVO 3/4: control_calidad_service.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/cocina/control_calidad_service.py
# ================================================================================

from src.patrones.observer.observer import IObserver
from src.patrones.observer.observable import IObservable
from src.entidades.cocina.orden_cocina import OrdenCocina
from src.entidades.cocina.estado_orden import EstadoOrden

class ControlCalidadService(IObserver):
    """
    Servicio Singleton que actúa como Observador.
    Puede "observar" órdenes de cocina y reaccionar cuando
    pasan al estado LISTA para verificar la calidad.
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
        print("Servicio de Control de Calidad inicializado.")

    def actualizar(self, observable: IObservable):
        """
        Método de IObserver. Se activa cuando un observable
        (ej. una OrdenCocina) notifica un cambio.
        """
        if not isinstance(observable, OrdenCocina):
            return
            
        orden = observable
        
        # Si la orden está LISTA, simular una verificación
        if orden.get_estado() == EstadoOrden.LISTA:
            self.verificar_orden(orden)
            
    def verificar_orden(self, orden: OrdenCocina):
        """
        Simula la lógica de control de calidad.
        """
        # Lógica de QC: ¿El plato cumple los estándares?
        # ¿Tiene las observaciones correctas?
        print(f"QC: Verificando Orden #{orden.get_id()}...")
        
        # Simulación de falla
        if "extra" in orden.get_observaciones_cliente().lower() and "extra" not in orden.get_notas_chef().lower():
             print(f"QC FALLIDO: Orden #{orden.get_id()} no tiene las notas de 'extra' aplicadas.")
             # Aquí se podría devolver la orden a EN_PREPARACION
        else:
             print(f"QC APROBADO: Orden #{orden.get_id()} lista para entregar.")

# ================================================================================
# ARCHIVO 4/4: distribucion_ordenes_service.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/cocina/distribucion_ordenes_service.py
# ================================================================================

from src.entidades.pedidos.pedido import Pedido
from src.entidades.cocina.orden_cocina import OrdenCocina
from src.servicios.cocina.cocina_service import CocinaService

class DistribucionOrdenesService:
    """
    Servicio Singleton que toma un Pedido y lo divide en
    múltiples OrdenCocina, enviándolas al CocinaService.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._cocina_service = CocinaService()
        self._inicializado = True

    def distribuir_pedido(self, pedido: Pedido):
        """
        Toma un pedido, crea las órdenes de cocina y las distribuye.
        """
        if not pedido.get_items():
            print(f"Advertencia: Pedido #{pedido.get_id()} no tiene items para distribuir.")
            return

        print(f"Distribuyendo Pedido #{pedido.get_id()} en órdenes de cocina...")
        
        for item_pedido in pedido.get_items():
            # Crear una OrdenCocina para cada ItemPedido
            orden = OrdenCocina(
                item_pedido=item_pedido,
                pedido_id=pedido.get_id(),
                mesa_id=pedido.get_mesa_id()
            )
            
            # Usar el CocinaService para enviar la orden
            try:
                self._cocina_service.enviar_orden_a_estacion(orden)
            except ValueError as e:
                print(f"Error al distribuir orden: {e}")
                # Aquí se podría manejar la lógica de un item que no
                # tiene estación (ej. cancelar la orden)

