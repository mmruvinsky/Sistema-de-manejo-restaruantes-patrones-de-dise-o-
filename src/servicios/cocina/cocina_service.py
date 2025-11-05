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