# src/entidades/cocina/estacion_cocina_general.py

from datetime import datetime
from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.constantes import TEMPERATURA_COCINA_MIN, TEMPERATURA_COCINA_MAX

class EstacionCocinaGeneral(EstacionCocina):
    """
    Estación de cocina general para items que no tienen
    una estación especializada (ej. Entradas, Pescados).
    Implementación concreta de EstacionCocina.
    """
    
    def __init__(self):
        # Llama al init de la clase base con sus valores
        super().__init__(nombre_estacion="Cocina", capacidad_maxima=10)
        self._ultima_limpieza = None
        # Asumimos que la cocina general empieza encendida
        self.set_activa(True) 
        self.set_temperatura_actual(22.0) # Temperatura ambiente
    
    # --- Implementación de métodos abstractos ---
    
    def verificar_equipamiento(self) -> bool:
        """
        Implementación simple: Asume que la cocina general
        siempre está operativa si está activa y en temperatura.
        """
        temp_ok = (TEMPERATURA_COCINA_MIN <= 
                   self.get_temperatura_actual() <= 
                   TEMPERATURA_COCINA_MAX)
        
        if not temp_ok:
            print(f"ALERTA: Temperatura fuera de rango en {self.get_nombre_estacion()}")
            
        return self.esta_activa() and temp_ok
    
    def realizar_mantenimiento(self):
        """Implementación simple: solo limpia órdenes completadas."""
        print(f"Realizando mantenimiento en {self.get_nombre_estacion()}...")
        self._ultima_limpieza = datetime.now()
        self.limpiar_ordenes_completadas()
    
    def obtener_temperatura_operacion(self) -> tuple:
        """Retorna el rango estándar de temperatura ambiente de cocina."""
        return (TEMPERATURA_COCINA_MIN, TEMPERATURA_COCINA_MAX)