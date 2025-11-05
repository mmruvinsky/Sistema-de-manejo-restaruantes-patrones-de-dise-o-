from datetime import datetime
from typing import Optional, List
from src.entidades.clientes.cliente import Cliente
from src.entidades.clientes.nivel_de_fidelidad import NivelDeFidelidad
from src.constantes import DESCUENTO_CLIENTE_FRECUENTE


class ClienteFrecuente(Cliente):
    """Cliente con programa de fidelidad"""
    
    def __init__(self, nombre: str, telefono: str, email: Optional[str] = None):
        super().__init__(nombre, telefono, email)
        self._puntos_acumulados = 0
        self._total_gastado = 0.0
        self._cantidad_visitas = 0
        self._nivel_fidelidad = NivelDeFidelidad.BRONCE
        self._fecha_ultima_visita: Optional[datetime] = None
        self._historial_visitas: List[datetime] = []
        self._codigo_qr = f"QR-{self._id:06d}"  # Código único para el cliente
    
    # --- GETTERS ---
    def get_puntos_acumulados(self) -> int:
        return self._puntos_acumulados
    
    def get_total_gastado(self) -> float:
        return self._total_gastado
    
    def get_cantidad_visitas(self) -> int:
        return self._cantidad_visitas
    
    def get_nivel_fidelidad(self) -> NivelDeFidelidad:
        return self._nivel_fidelidad
    
    def get_fecha_ultima_visita(self) -> Optional[datetime]:
        return self._fecha_ultima_visita
    
    def get_codigo_qr(self) -> str:
        return self._codigo_qr
    
    def get_historial_visitas(self) -> List[datetime]:
        return self._historial_visitas.copy()
    
    # --- MÉTODOS DE PUNTOS Y FIDELIDAD ---
    def agregar_puntos(self, puntos: int):
        """Agrega puntos de fidelidad"""
        if puntos < 0:
            raise ValueError("Los puntos no pueden ser negativos")
        self._puntos_acumulados += puntos
    
    def canjear_puntos(self, puntos: int) -> bool:
        """Canjea puntos por beneficios"""
        if puntos < 0:
            raise ValueError("Los puntos a canjear deben ser positivos")
        if self._puntos_acumulados >= puntos:
            self._puntos_acumulados -= puntos
            return True
        return False
    
    def registrar_visita(self, monto_gastado: float):
        """Registra una nueva visita y actualiza estadísticas"""
        self._cantidad_visitas += 1
        self._total_gastado += monto_gastado
        self._fecha_ultima_visita = datetime.now()
        self._historial_visitas.append(self._fecha_ultima_visita)
        
        # Calcular puntos: 1 punto por cada $10 gastados
        puntos_ganados = int(monto_gastado / 10)
        self.agregar_puntos(puntos_ganados)
        
        # Actualizar nivel de fidelidad
        self._actualizar_nivel_fidelidad()
    
    def _actualizar_nivel_fidelidad(self):
        """Actualiza el nivel de fidelidad según visitas"""
        nuevo_nivel = NivelDeFidelidad.obtener_nivel_por_visitas(self._cantidad_visitas)
        if nuevo_nivel != self._nivel_fidelidad:
            self._nivel_fidelidad = nuevo_nivel
    
    def calcular_promedio_gasto(self) -> float:
        """Calcula el gasto promedio por visita"""
        if self._cantidad_visitas == 0:
            return 0.0
        return self._total_gastado / self._cantidad_visitas
    
    def dias_desde_ultima_visita(self) -> Optional[int]:
        """Retorna los días desde la última visita"""
        if not self._fecha_ultima_visita:
            return None
        delta = datetime.now() - self._fecha_ultima_visita
        return delta.days
    
    def esta_inactivo(self, dias_limite: int = 90) -> bool:
        """Verifica si el cliente está inactivo (sin visitas por X días)"""
        dias = self.dias_desde_ultima_visita()
        if dias is None:
            return True
        return dias > dias_limite
    
    # --- OVERRIDE DE MÉTODOS DE CLIENTE ---
    def es_cliente_frecuente(self) -> bool:
        """Override - siempre retorna True"""
        return True
    
    def aplicar_descuento(self) -> float:
        """Retorna el porcentaje de descuento según nivel de fidelidad"""
        # Puede usar el descuento del nivel o el constante general
        return max(self._nivel_fidelidad.descuento, DESCUENTO_CLIENTE_FRECUENTE)
    
    # --- BENEFICIOS Y RECOMPENSAS ---
    def puede_canjear_comida_gratis(self) -> bool:
        """Verifica si tiene suficientes puntos para comida gratis (500 puntos)"""
        return self._puntos_acumulados >= 500
    
    def puede_canjear_bebida_gratis(self) -> bool:
        """Verifica si tiene suficientes puntos para bebida gratis (200 puntos)"""
        return self._puntos_acumulados >= 200
    
    def puede_canjear_postre_gratis(self) -> bool:
        """Verifica si tiene suficientes puntos para postre gratis (150 puntos)"""
        return self._puntos_acumulados >= 150
    
    def obtener_beneficios_disponibles(self) -> List[str]:
        """Retorna lista de beneficios que puede canjear"""
        beneficios = []
        if self.puede_canjear_comida_gratis():
            beneficios.append("🍽️ Comida gratis (500 pts)")
        if self.puede_canjear_bebida_gratis():
            beneficios.append("🍷 Bebida gratis (200 pts)")
        if self.puede_canjear_postre_gratis():
            beneficios.append("🍰 Postre gratis (150 pts)")
        return beneficios
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        
        ultima_visita = (self._fecha_ultima_visita.strftime('%d/%m/%Y') 
                        if self._fecha_ultima_visita else "Nunca")
        
        beneficios = self.obtener_beneficios_disponibles()
        beneficios_str = "\n    " + "\n    ".join(beneficios) if beneficios else ""
        
        return (f"{base_str}\n"
                f"  {self._nivel_fidelidad}\n"
                f"  Puntos: {self._puntos_acumulados} pts\n"
                f"  Visitas: {self._cantidad_visitas}\n"
                f"  Total gastado: ${self._total_gastado:.2f}\n"
                f"  Promedio por visita: ${self.calcular_promedio_gasto():.2f}\n"
                f"  Última visita: {ultima_visita}\n"
                f"  Descuento: {self.aplicar_descuento()}%\n"
                f"  Código QR: {self._codigo_qr}"
                f"{beneficios_str}")
    
    def __repr__(self) -> str:
        return (f"ClienteFrecuente(id={self._id}, "
                f"nombre='{self._nombre}', "
                f"nivel={self._nivel_fidelidad.nombre_nivel})")