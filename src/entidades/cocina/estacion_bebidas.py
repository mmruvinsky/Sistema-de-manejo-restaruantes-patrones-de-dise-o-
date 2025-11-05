from datetime import datetime
from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.entidades.cocina.orden_cocina import OrdenCocina

class EstacionBebidas(EstacionCocina):
    """Estación especializada en bebidas (barra)"""
    
    def __init__(self):
        super().__init__(nombre_estacion="Bebidas", capacidad_maxima=10)
        self._hielo_disponible_kg = 50.0
        self._copas_limpias = 100
        self._vasos_limpios = 150
        self._maquina_cafe_encendida = True
        self._ultima_limpieza = None
    
    # --- GETTERS ESPECÍFICOS ---
    def get_hielo_disponible(self) -> float:
        return self._hielo_disponible_kg
    
    def get_copas_limpias(self) -> int:
        return self._copas_limpias
    
    def get_vasos_limpios(self) -> int:
        return self._vasos_limpios
    
    def esta_maquina_cafe_encendida(self) -> bool:
        return self._maquina_cafe_encendida
    
    # --- OPERACIONES ---
    def agregar_hielo(self, cantidad_kg: float):
        """Agrega hielo"""
        if cantidad_kg <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self._hielo_disponible_kg += cantidad_kg
    
    def consumir_hielo(self, cantidad_kg: float = 0.2):
        """Consume hielo al preparar bebida"""
        if self._hielo_disponible_kg < cantidad_kg:
            raise ValueError("No hay suficiente hielo")
        self._hielo_disponible_kg -= cantidad_kg
    
    def usar_copa(self):
        """Usa una copa"""
        if self._copas_limpias <= 0:
            raise ValueError("No hay copas limpias")
        self._copas_limpias -= 1
    
    def usar_vaso(self):
        """Usa un vaso"""
        if self._vasos_limpios <= 0:
            raise ValueError("No hay vasos limpios")
        self._vasos_limpios -= 1
    
    def lavar_cristaleria(self, copas: int = 0, vasos: int = 0):
        """Agrega copas y vasos limpios"""
        self._copas_limpias += copas
        self._vasos_limpios += vasos
    
    # --- OVERRIDE DE MÉTODOS ABSTRACTOS ---
    def verificar_equipamiento(self) -> bool:
        """Verifica que se pueda preparar bebidas"""
        if not self._maquina_cafe_encendida:
            return False
        if self._hielo_disponible_kg < 1.0:
            return False
        if self._copas_limpias + self._vasos_limpios < 10:
            return False
        return True
    
    def realizar_mantenimiento(self):
        """Realiza limpieza de la barra"""
        self._ultima_limpieza = datetime.now()
        self.limpiar_ordenes_completadas()
    
    def obtener_temperatura_operacion(self) -> tuple:
        """Rango óptimo de temperatura"""
        return (18, 25)  # °C
    
    # --- VALIDACIONES ---
    def necesita_hielo(self) -> bool:
        """Verifica si necesita hielo"""
        return self._hielo_disponible_kg < 10.0
    
    def necesita_cristaleria(self) -> bool:
        """Verifica si necesita lavar cristalería"""
        return (self._copas_limpias < 20 or self._vasos_limpios < 30)
    
    def puede_preparar_bebidas(self) -> bool:
        """Verifica si puede preparar bebidas"""
        return (self._hielo_disponible_kg >= 0.2 and 
                (self._copas_limpias > 0 or self._vasos_limpios > 0))
    
    # --- OVERRIDE DE COMPLETAR ORDEN ---
    def completar_orden(self, orden_id: int):
        """Override para consumir recursos"""
        resultado = super().completar_orden(orden_id)
        if resultado:
            # Lógica simplificada: alternamos entre copa y vaso
            if self._copas_limpias > 0:
                self.usar_copa()
            else:
                self.usar_vaso()
            self.consumir_hielo(0.1)
        return resultado
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        
        hielo_alerta = "⚠️ BAJO" if self.necesita_hielo() else "✓"
        cristal_alerta = "⚠️ LAVAR" if self.necesita_cristaleria() else "✓"
        cafe = "☕ Encendida" if self._maquina_cafe_encendida else "☕ Apagada"
        
        return (f"{base_str}\n"
                f"  Máquina café: {cafe}\n"
                f"  Hielo: {self._hielo_disponible_kg:.1f} kg {hielo_alerta}\n"
                f"  Copas: {self._copas_limpias} | Vasos: {self._vasos_limpios} {cristal_alerta}")
    
    def __repr__(self) -> str:
        return f"EstacionBebidas(ordenes={self.contar_ordenes_totales()}, hielo={self._hielo_disponible_kg:.1f}kg)"