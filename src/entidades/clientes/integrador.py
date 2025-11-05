"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/clientes
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/clientes/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: cliente.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/clientes/cliente.py
# ================================================================================

from datetime import datetime
from typing import Optional

class Cliente:
    """Representa un cliente del restaurante"""
    
    _contador_id = 0
    
    def __init__(self, nombre: str, telefono: str, email: Optional[str] = None):
        Cliente._contador_id += 1
        self._id = Cliente._contador_id
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
        self._fecha_registro = datetime.now()
        self._direccion = ""
        self._notas = ""  # Preferencias, alergias, etc.
        self._activo = True
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_telefono(self) -> str:
        return self._telefono
    
    def get_email(self) -> Optional[str]:
        return self._email
    
    def get_fecha_registro(self) -> datetime:
        return self._fecha_registro
    
    def get_direccion(self) -> str:
        return self._direccion
    
    def get_notas(self) -> str:
        return self._notas
    
    def esta_activo(self) -> bool:
        return self._activo
    
    # --- SETTERS ---
    def set_nombre(self, nombre: str):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre
    
    def set_telefono(self, telefono: str):
        if not telefono or telefono.strip() == "":
            raise ValueError("El teléfono no puede estar vacío")
        self._telefono = telefono
    
    def set_email(self, email: str):
        self._email = email
    
    def set_direccion(self, direccion: str):
        self._direccion = direccion
    
    def set_notas(self, notas: str):
        """Notas sobre preferencias, alergias, etc."""
        self._notas = notas
    
    def set_activo(self, activo: bool):
        self._activo = activo
    
    # --- MÉTODOS ---
    def agregar_nota(self, nota: str):
        """Agrega una nota adicional a las existentes"""
        if self._notas:
            self._notas += f"\n- {nota}"
        else:
            self._notas = f"- {nota}"
    
    def tiempo_como_cliente(self) -> int:
        """Retorna los días desde el registro"""
        delta = datetime.now() - self._fecha_registro
        return delta.days
    
    def es_cliente_frecuente(self) -> bool:
        """Método base - se sobrescribe en ClienteFrecuente"""
        return False
    
    def aplicar_descuento(self) -> float:
        """Método base - clientes normales no tienen descuento"""
        return 0.0
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado = "✅ Activo" if self._activo else "❌ Inactivo"
        email_str = f"\n  Email: {self._email}" if self._email else ""
        direccion_str = f"\n  Dirección: {self._direccion}" if self._direccion else ""
        notas_str = f"\n  Notas: {self._notas}" if self._notas else ""
        
        return (f"👤 Cliente #{self._id}\n"
                f"  Nombre: {self._nombre}\n"
                f"  Teléfono: {self._telefono}"
                f"{email_str}"
                f"{direccion_str}"
                f"  Estado: {estado}\n"
                f"  Cliente desde: {self._fecha_registro.strftime('%d/%m/%Y')}"
                f"{notas_str}")
    
    def __repr__(self) -> str:
        return f"Cliente(id={self._id}, nombre='{self._nombre}')"

# ================================================================================
# ARCHIVO 3/4: cliente_frecuente.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/clientes/cliente_frecuente.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: nivel_de_fidelidad.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/clientes/nivel_de_fidelidad.py
# ================================================================================

from enum import Enum

class NivelDeFidelidad(Enum):
    """Niveles de fidelidad para clientes frecuentes"""
    BRONCE = ("Bronce", 5, "🥉")      # nivel, descuento%, emoji
    PLATA = ("Plata", 10, "🥈")
    ORO = ("Oro", 15, "🥇")
    PLATINO = ("Platino", 20, "💎")
    
    def __init__(self, nombre: str, descuento: int, emoji: str):
        self._nombre_nivel = nombre
        self._descuento = descuento
        self._emoji = emoji
    
    @property
    def nombre_nivel(self) -> str:
        return self._nombre_nivel
    
    @property
    def descuento(self) -> int:
        """Porcentaje de descuento"""
        return self._descuento
    
    @property
    def emoji(self) -> str:
        return self._emoji
    
    def __str__(self):
        return f"{self._emoji} {self._nombre_nivel}"
    
    @classmethod
    def obtener_nivel_por_visitas(cls, cantidad_visitas: int):
        """Determina el nivel según la cantidad de visitas"""
        if cantidad_visitas >= 50:
            return cls.PLATINO
        elif cantidad_visitas >= 30:
            return cls.ORO
        elif cantidad_visitas >= 15:
            return cls.PLATA
        else:
            return cls.BRONCE

