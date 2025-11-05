from datetime import datetime
from typing import Optional
from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.entidades.cocina.orden_cocina import OrdenCocina

class EstacionPastas(EstacionCocina):
    """Estación especializada en pastas"""
    
    def __init__(self):
        super().__init__(nombre_estacion="Pastas", capacidad_maxima=6)
        self._agua_hirviendo = False
        self._ollas_disponibles = 4
        self._cantidad_pasta_kg = 50.0  # kg disponibles
        self._ultima_limpieza = None
    
    # --- GETTERS ESPECÍFICOS ---
    def get_ollas_disponibles(self) -> int:
        return self._ollas_disponibles
    
    def get_cantidad_pasta(self) -> float:
        return self._cantidad_pasta_kg
    
    def esta_agua_hirviendo(self) -> bool:
        return self._agua_hirviendo
    
    # --- OPERACIONES ---
    def calentar_agua(self):
        """Calienta el agua para cocinar"""
        self._agua_hirviendo = True
        self._temperatura_actual = 100.0
    
    def enfriar_agua(self):
        """Enfría el agua"""
        self._agua_hirviendo = False
        self._temperatura_actual = 20.0
    
    def agregar_pasta(self, cantidad_kg: float):
        """Agrega pasta al inventario"""
        if cantidad_kg <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self._cantidad_pasta_kg += cantidad_kg
    
    def consumir_pasta(self, cantidad_kg: float = 0.3):
        """Consume pasta al preparar un plato"""
        if self._cantidad_pasta_kg < cantidad_kg:
            raise ValueError("No hay suficiente pasta")
        self._cantidad_pasta_kg -= cantidad_kg
    
    def usar_olla(self):
        """Marca una olla como en uso"""
        if self._ollas_disponibles <= 0:
            raise ValueError("No hay ollas disponibles")
        self._ollas_disponibles -= 1
    
    def liberar_olla(self):
        """Libera una olla"""
        if self._ollas_disponibles >= 4:
            raise ValueError("Todas las ollas ya están libres")
        self._ollas_disponibles += 1
    
    # --- OVERRIDE DE MÉTODOS ABSTRACTOS ---
    def verificar_equipamiento(self) -> bool:
        """Verifica que se pueda cocinar pasta"""
        if not self._agua_hirviendo:
            return False
        if self._ollas_disponibles <= 0:
            return False
        if self._cantidad_pasta_kg < 1.0:
            return False
        return True
    
    def realizar_mantenimiento(self):
        """Realiza limpieza de la estación"""
        self._ultima_limpieza = datetime.now()
        self.limpiar_ordenes_completadas()
    
    def obtener_temperatura_operacion(self) -> tuple:
        """Rango óptimo de temperatura"""
        return (18, 28)  # °C ambiente
    
    # --- VALIDACIONES ---
    def necesita_pasta(self) -> bool:
        """Verifica si necesita reposición de pasta"""
        return self._cantidad_pasta_kg < 10.0
    
    def puede_cocinar_pasta(self) -> bool:
        """Verifica si puede cocinar pasta"""
        return (self._agua_hirviendo and 
                self._ollas_disponibles > 0 and 
                self._cantidad_pasta_kg >= 0.3)
    
    # --- OVERRIDE DE COMPLETAR ORDEN ---
    def completar_orden(self, orden_id: int):
        """Override para liberar olla y consumir pasta"""
        resultado = super().completar_orden(orden_id)
        if resultado:
            self.liberar_olla()
            self.consumir_pasta()
        return resultado
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        agua_estado = "💧 Hirviendo" if self._agua_hirviendo else "💧 Fría"
        pasta_alerta = "⚠️ BAJO" if self.necesita_pasta() else "✓"
        
        return (f"{base_str}\n"
                f"  Agua: {agua_estado}\n"
                f"  Ollas disponibles: {self._ollas_disponibles}/4\n"
                f"  Pasta: {self._cantidad_pasta_kg:.1f} kg {pasta_alerta}")
    
    def __repr__(self) -> str:
        return f"EstacionPastas(ordenes={self.contar_ordenes_totales()}, pasta={self._cantidad_pasta_kg:.1f}kg)"
