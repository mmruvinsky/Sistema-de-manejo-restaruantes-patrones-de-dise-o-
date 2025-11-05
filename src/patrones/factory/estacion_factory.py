# src/patrones/factory/estacion_factory.py

from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.entidades.cocina.estacion_parrilla import EstacionParrilla 
from src.entidades.cocina.estacion_pastas import EstacionPastas 
from src.entidades.cocina.estacion_postres import EstacionPostres 
from src.entidades.cocina.estacion_bebidas import EstacionBebidas 

# --- IMPORTACIÓN AÑADIDA ---
# Importamos la nueva clase CONCRETA
from src.entidades.cocina.estacion_cocina_general import EstacionCocinaGeneral
# (Asegúrate de que la ruta de importación sea correcta según dónde guardaste el archivo)


class EstacionFactory:
    """
    Patrón Simple Factory para crear instancias de EstacionCocina.
    """
    
    @staticmethod
    def crear_estacion(nombre_estacion: str) -> EstacionCocina:
        """
        Crea y retorna un objeto EstacionCocina basado en su nombre.
        
        El 'nombre_estacion' proviene de los métodos 
        get_estacion_cocina() de tus ItemMenu.
        """
        nombre_normalizado = nombre_estacion.lower()
        
        if nombre_normalizado == "parrilla":
            return EstacionParrilla()
        
        elif nombre_normalizado == "pastas":
            return EstacionPastas()
            
        elif nombre_normalizado == "postres":
            return EstacionPostres()
        
        elif nombre_normalizado == "bebidas":
            return EstacionBebidas()
        
        # --- LÍNEA CORREGIDA ---
        elif nombre_normalizado == "cocina":
            # Para 'Entrada' y ahora 'Pescado'
            return EstacionCocinaGeneral() # Usamos la clase concreta
        
        # El caso "plancha" se ha eliminado
        
        else:
            raise ValueError(f"Tipo de estación desconocida: {nombre_estacion}")