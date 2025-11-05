from datetime import datetime
from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.entidades.cocina.orden_cocina import OrdenCocina

class EstacionPostres(EstacionCocina):
    """Estación especializada en postres"""
    
    def __init__(self):
        super().__init__(nombre_estacion="Postres", capacidad_maxima=5)
        self._heladera_encendida = True
        self._temperatura_heladera = -5.0  # °C
        self._horno_encendido = False
        self._temperatura_horno = 0.0
        self._ultima_limpieza = None
    
    # --- GETTERS ESPECÍFICOS ---
    def get_temperatura_heladera(self) -> float:
        return self._temperatura_heladera
    
    def get_temperatura_horno(self) -> float:
        return self._temperatura_horno
    
    def esta_heladera_encendida(self) -> bool:
        return self._heladera_encendida
    
    def esta_horno_encendido(self) -> bool:
        return self._horno_encendido
    
    # --- OPERACIONES ---
    def encender_horno(self, temperatura: float = 180.0):
        """Enciende el horno de postres"""
        if temperatura < 100 or temperatura > 250:
            raise ValueError("Temperatura fuera de rango (100-250°C)")
        self._horno_encendido = True
        self._temperatura_horno = temperatura
    
    def apagar_horno(self):
        """Apaga el horno"""
        self._horno_encendido = False
        self._temperatura_horno = 0.0
    
    def ajustar_temperatura_horno(self, temperatura: float):
        """Ajusta la temperatura del horno"""
        if not self._horno_encendido:
            raise ValueError("El horno no está encendido")
        if temperatura < 100 or temperatura > 250:
            raise ValueError("Temperatura fuera de rango")
        self._temperatura_horno = temperatura
    
    def ajustar_temperatura_heladera(self, temperatura: float):
        """Ajusta la temperatura de la heladera"""
        if temperatura > 5:
            raise ValueError("La heladera debe estar bajo 5°C")
        self._temperatura_heladera = temperatura
    
    # --- OVERRIDE DE MÉTODOS ABSTRACTOS ---
    def verificar_equipamiento(self) -> bool:
        """Verifica que el equipamiento esté funcionando"""
        if not self._heladera_encendida:
            return False
        if self._temperatura_heladera > 5:
            return False
        return True
    
    def realizar_mantenimiento(self):
        """Realiza mantenimiento de la estación"""
        self._ultima_limpieza = datetime.now()
        self.limpiar_ordenes_completadas()
    
    def obtener_temperatura_operacion(self) -> tuple:
        """Rango óptimo de temperatura ambiente"""
        return (18, 24)  # °C
    
    # --- VALIDACIONES ---
    def puede_hacer_postres_frios(self) -> bool:
        """Verifica si puede hacer postres fríos"""
        return self._heladera_encendida and self._temperatura_heladera <= 0
    
    def puede_hornear(self) -> bool:
        """Verifica si puede hornear postres"""
        return self._horno_encendido and self._temperatura_horno >= 150
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        
        heladera_estado = f"❄️ {self._temperatura_heladera}°C" if self._heladera_encendida else "❄️ Apagada"
        horno_estado = f"🔥 {self._temperatura_horno}°C" if self._horno_encendido else "🔥 Apagado"
        
        return (f"{base_str}\n"
                f"  Heladera: {heladera_estado}\n"
                f"  Horno: {horno_estado}")
    
    def __repr__(self) -> str:
        return f"EstacionPostres(ordenes={self.contar_ordenes_totales()})"