from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.entidades.cocina.estacion_parrilla import EstacionParrilla 
from src.entidades.cocina.estacion_pastas import EstacionPastas 
from src.entidades.cocina.estacion_postres import EstacionPostres 
from src.entidades.cocina.estacion_bebidas import EstacionBebidas 
from src.entidades.cocina.estacion_cocina import EstacionCocina


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
        
        elif nombre_normalizado == "cocina":
            # Para 'Entrada'
            return EstacionCocina()
        
        else:
            raise ValueError(f"Tipo de estación desconocida: {nombre_estacion}")