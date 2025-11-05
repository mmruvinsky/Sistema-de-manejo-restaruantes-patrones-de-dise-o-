from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.constantes import TEMPERATURA_PARRILLA


class EstacionParrilla(EstacionCocina):
    """Estación especializada en parrilla (carnes y pollo)"""
    
    def __init__(self):
        super().__init__(nombre_estacion="Parrilla", capacidad_maxima=8)
        self._temperatura_parrilla = TEMPERATURA_PARRILLA
        self._carbon_disponible = 100.0  # kg
        self._parrilla_encendida = False
        self._ultima_limpieza = None
    
    # --- GETTERS ESPECÍFICOS ---
    def get_temperatura_parrilla(self) -> float:
        return self._temperatura_parrilla
    
    def get_carbon_disponible(self) -> float:
        return self._carbon_disponible
    
    def esta_parrilla_encendida(self) -> bool:
        return self._parrilla_encendida
    
    # --- SETTERS ESPECÍFICOS ---
    def set_temperatura_parrilla(self, temperatura: float):
        if temperatura < 150 or temperatura > 300:
            raise ValueError("Temperatura de parrilla fuera de rango (150-300°C)")
        self._temperatura_parrilla = temperatura
    
    def encender_parrilla(self):
        """Enciende la parrilla"""
        if self._carbon_disponible < 5:
            raise ValueError("No hay suficiente carbón para encender la parrilla")
        self._parrilla_encendida = True
        self._temperatura_parrilla = TEMPERATURA_PARRILLA
    
    def apagar_parrilla(self):
        """Apaga la parrilla"""
        self._parrilla_encendida = False
        self._temperatura_parrilla = self._temperatura_actual
    
    def agregar_carbon(self, cantidad: float):
        """Agrega carbón a la parrilla"""
        if cantidad <= 0:
            raise ValueError("La cantidad de carbón debe ser positiva")
        self._carbon_disponible += cantidad
    
    def consumir_carbon(self, cantidad: float = 2.0):
        """Consume carbón durante la cocción"""
        if self._carbon_disponible < cantidad:
            raise ValueError("No hay suficiente carbón")
        self._carbon_disponible -= cantidad
    
    # --- OVERRIDE DE MÉTODOS ABSTRACTOS ---
    def verificar_equipamiento(self) -> bool:
        """Verifica que la parrilla esté en condiciones de operar"""
        if not self._parrilla_encendida:
            return False
        
        if self._carbon_disponible < 10:
            return False
        
        if self._temperatura_parrilla < 150:
            return False
        
        return True
    
    def realizar_mantenimiento(self):
        """Realiza limpieza y mantenimiento de la parrilla"""
        from datetime import datetime
        self._ultima_limpieza = datetime.now()
        # Limpiar órdenes completadas
        self.limpiar_ordenes_completadas()
    
    def obtener_temperatura_operacion(self) -> tuple:
        """Retorna rango de temperatura óptima de operación"""
        return (180, 220)  # °C
    
    # --- MÉTODOS ESPECÍFICOS ---
    def puede_cocinar_a_la_parrilla(self) -> bool:
        """Verifica si se puede cocinar (parrilla encendida y con carbón)"""
        return (self._parrilla_encendida and 
                self._carbon_disponible >= 5 and 
                self._temperatura_parrilla >= 150)
    
    def necesita_carbon(self) -> bool:
        """Verifica si necesita reposición de carbón"""
        return self._carbon_disponible < 20
    
    def ajustar_temperatura(self, incremento: float):
        """Ajusta la temperatura de la parrilla"""
        nueva_temp = self._temperatura_parrilla + incremento
        self.set_temperatura_parrilla(nueva_temp)
    
    # --- OVERRIDE DE RECIBIR ORDEN ---
    def recibir_orden(self, orden):
        """Override para verificar que la parrilla esté lista"""
        if not self.puede_cocinar_a_la_parrilla():
            raise ValueError("La parrilla no está lista para cocinar")
        super().recibir_orden(orden)
    
    # --- OVERRIDE DE COMPLETAR ORDEN ---
    def completar_orden(self, orden_id: int):
        """Override para consumir carbón al completar"""
        resultado = super().completar_orden(orden_id)
        if resultado:
            self.consumir_carbon(1.5)  # Consume carbón por orden
        return resultado
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        
        parrilla_estado = "🔥 Encendida" if self._parrilla_encendida else "⚫ Apagada"
        carbon_alerta = "⚠️ BAJO" if self.necesita_carbon() else "✓"
        
        return (f"{base_str}\n"
                f"  Parrilla: {parrilla_estado}\n"
                f"  Temp. Parrilla: {self._temperatura_parrilla}°C\n"
                f"  Carbón: {self._carbon_disponible:.1f} kg {carbon_alerta}")
    
    def __repr__(self) -> str:
        return f"EstacionParrilla(ordenes={self.contar_ordenes_totales()}, carbon={self._carbon_disponible:.1f}kg)"