"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/inventario
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/inventario/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: alerta_stock.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/inventario/alerta_stock.py
# ================================================================================

from datetime import datetime
from enum import Enum
from typing import Optional


class TipoAlerta(Enum):
    """Tipos de alertas de stock"""
    STOCK_BAJO = ("Stock Bajo", "🟡", 2)  # tipo, emoji, prioridad
    STOCK_CRITICO = ("Stock Crítico", "🟠", 3)
    AGOTADO = ("Agotado", "🔴", 5)
    POR_VENCER = ("Por Vencer", "⏰", 3)
    VENCIDO = ("Vencido", "⚠️", 5)
    SOBRESTOCK = ("Sobrestock", "📈", 1)
    
    def __init__(self, descripcion: str, emoji: str, prioridad: int):
        self._descripcion = descripcion
        self._emoji = emoji
        self._prioridad = prioridad
    
    @property
    def descripcion(self) -> str:
        return self._descripcion
    
    @property
    def emoji(self) -> str:
        return self._emoji
    
    @property
    def prioridad(self) -> int:
        """Prioridad de 1 (baja) a 5 (crítica)"""
        return self._prioridad
    
    def __str__(self):
        return f"{self._emoji} {self._descripcion}"


class AlertaStock:
    """Representa una alerta del sistema de inventario"""
    
    _contador_id = 0
    
    def __init__(self, ingrediente_id: int, ingrediente_nombre: str, 
                 tipo_alerta: TipoAlerta, mensaje: str):
        AlertaStock._contador_id += 1
        self._id = AlertaStock._contador_id
        self._ingrediente_id = ingrediente_id
        self._ingrediente_nombre = ingrediente_nombre
        self._tipo_alerta = tipo_alerta
        self._mensaje = mensaje
        self._fecha_hora_generacion = datetime.now()
        self._resuelta = False
        self._fecha_hora_resolucion: Optional[datetime] = None
        self._accion_tomada = ""
        self._usuario_responsable_id: Optional[int] = None
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_ingrediente_id(self) -> int:
        return self._ingrediente_id
    
    def get_ingrediente_nombre(self) -> str:
        return self._ingrediente_nombre
    
    def get_tipo_alerta(self) -> TipoAlerta:
        return self._tipo_alerta
    
    def get_mensaje(self) -> str:
        return self._mensaje
    
    def get_fecha_hora_generacion(self) -> datetime:
        return self._fecha_hora_generacion
    
    def esta_resuelta(self) -> bool:
        return self._resuelta
    
    def get_fecha_hora_resolucion(self) -> Optional[datetime]:
        return self._fecha_hora_resolucion
    
    def get_accion_tomada(self) -> str:
        return self._accion_tomada
    
    def get_prioridad(self) -> int:
        """Retorna la prioridad de la alerta"""
        return self._tipo_alerta.prioridad
    
    # --- SETTERS ---
    def resolver(self, accion_tomada: str, usuario_id: Optional[int] = None):
        """Marca la alerta como resuelta"""
        if self._resuelta:
            raise ValueError("La alerta ya está resuelta")
        
        self._resuelta = True
        self._fecha_hora_resolucion = datetime.now()
        self._accion_tomada = accion_tomada
        self._usuario_responsable_id = usuario_id
    
    def reabrir(self):
        """Reabre una alerta resuelta"""
        if not self._resuelta:
            raise ValueError("La alerta no está resuelta")
        
        self._resuelta = False
        self._fecha_hora_resolucion = None
        self._accion_tomada = ""
        self._usuario_responsable_id = None
    
    # --- CÁLCULOS ---
    def calcular_tiempo_sin_resolver(self) -> int:
        """Calcula los minutos desde que se generó la alerta"""
        if self._resuelta:
            return 0
        delta = datetime.now() - self._fecha_hora_generacion
        return int(delta.total_seconds() / 60)
    
    def calcular_tiempo_resolucion(self) -> Optional[int]:
        """Calcula los minutos que tomó resolver la alerta"""
        if not self._resuelta or not self._fecha_hora_resolucion:
            return None
        delta = self._fecha_hora_resolucion - self._fecha_hora_generacion
        return int(delta.total_seconds() / 60)
    
    def es_critica(self) -> bool:
        """Verifica si la alerta es de prioridad crítica (4 o 5)"""
        return self._tipo_alerta.prioridad >= 4
    
    def es_antigua(self, horas_limite: int = 24) -> bool:
        """Verifica si la alerta lleva mucho tiempo sin resolver"""
        if self._resuelta:
            return False
        horas = self.calcular_tiempo_sin_resolver() / 60
        return horas > horas_limite
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado = "✅ Resuelta" if self._resuelta else "⏳ Pendiente"
        
        tiempo_info = ""
        if self._resuelta:
            tiempo_resol = self.calcular_tiempo_resolucion()
            if tiempo_resol is not None:
                tiempo_info = f"\n  ⏱️ Tiempo de resolución: {tiempo_resol} min"
                tiempo_info += f"\n  ✓ Acción: {self._accion_tomada}"
        else:
            minutos = self.calcular_tiempo_sin_resolver()
            tiempo_info = f"\n  ⏱️ Sin resolver: {minutos} min"
            if self.es_antigua():
                tiempo_info += " ⚠️ ANTIGUA"
        
        return (f"{self._tipo_alerta} - Alerta #{self._id}\n"
                f"  Ingrediente: {self._ingrediente_nombre}\n"
                f"  {self._mensaje}\n"
                f"  Estado: {estado}\n"
                f"  Prioridad: {self._tipo_alerta.prioridad}/5\n"
                f"  Generada: {self._fecha_hora_generacion.strftime('%d/%m/%Y %H:%M')}"
                f"{tiempo_info}")
    
    def __repr__(self) -> str:
        return (f"AlertaStock(id={self._id}, "
                f"tipo={self._tipo_alerta.descripcion}, "
                f"ingrediente='{self._ingrediente_nombre}', "
                f"resuelta={self._resuelta})")
    
    # --- COMPARACIÓN PARA ORDENAMIENTO ---
    def __lt__(self, other):
        """Permite ordenar alertas por prioridad (mayor prioridad primero)"""
        if not isinstance(other, AlertaStock):
            return NotImplemented
        return self._tipo_alerta.prioridad > other._tipo_alerta.prioridad

# ================================================================================
# ARCHIVO 3/5: categoria_ingrediente.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/inventario/categoria_ingrediente.py
# ================================================================================

from enum import Enum

class CategoriaIngrediente(Enum):
    """Categorías de ingredientes para el inventario"""
    CARNES = "Carnes"
    PESCADOS_MARISCOS = "Pescados y Mariscos"
    VERDURAS = "Verduras"
    FRUTAS = "Frutas"
    LACTEOS = "Lácteos"
    CEREALES_GRANOS = "Cereales y Granos"
    ESPECIAS_CONDIMENTOS = "Especias y Condimentos"
    ACEITES_SALSAS = "Aceites y Salsas"
    BEBIDAS = "Bebidas"
    PANADERIA = "Panadería"
    POSTRES_DULCES = "Postres y Dulces"
    OTROS = "Otros"
    
    def __str__(self):
        return self.value
    
    @classmethod
    def obtener_categorias(cls):
        """Retorna lista de todas las categorías"""
        return [cat.value for cat in cls]

# ================================================================================
# ARCHIVO 4/5: ingrediente.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/inventario/ingrediente.py
# ================================================================================

from datetime import datetime, timedelta
from typing import Optional
from src.entidades.inventario.unidad_medida import UnidadMedida
from src.entidades.inventario.categoria_ingrediente import CategoriaIngrediente
from src.constantes import STOCK_MINIMO_INGREDIENTE, STOCK_CRITICO, DIAS_VENCIMIENTO_ALERTA
from src.patrones.observer.observable import Observable


class Ingrediente(Observable):
    """Representa un ingrediente en el inventario del restaurante"""
    
    _contador_id = 0
    
    def __init__(self, nombre: str, categoria: CategoriaIngrediente, 
                 unidad_medida: UnidadMedida, cantidad_actual: float):
        super().__init__()
        Ingrediente._contador_id += 1
        self._id = Ingrediente._contador_id
        self._nombre = nombre
        self._categoria = categoria
        self._unidad_medida = unidad_medida
        self._cantidad_actual = cantidad_actual
        self._cantidad_minima = STOCK_MINIMO_INGREDIENTE
        self._cantidad_maxima = cantidad_actual * 3  # Por defecto, 3x el stock inicial
        self._precio_unitario = 0.0
        self._proveedor = ""
        self._fecha_ultimo_reabastecimiento: Optional[datetime] = None
        self._fecha_vencimiento: Optional[datetime] = None
        self._ubicacion_almacen = ""
        self._requiere_refrigeracion = False
        self._notas = ""
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_categoria(self) -> CategoriaIngrediente:
        return self._categoria
    
    def get_unidad_medida(self) -> UnidadMedida:
        return self._unidad_medida
    
    def get_cantidad_actual(self) -> float:
        return self._cantidad_actual
    
    def get_cantidad_minima(self) -> float:
        return self._cantidad_minima
    
    def get_cantidad_maxima(self) -> float:
        return self._cantidad_maxima
    
    def get_precio_unitario(self) -> float:
        return self._precio_unitario
    
    def get_proveedor(self) -> str:
        return self._proveedor
    
    def get_fecha_vencimiento(self) -> Optional[datetime]:
        return self._fecha_vencimiento
    
    def get_ubicacion_almacen(self) -> str:
        return self._ubicacion_almacen
    
    def requiere_refrigeracion(self) -> bool:
        return self._requiere_refrigeracion
    
    def get_notas(self) -> str:
        return self._notas
    
    # --- SETTERS ---
    def set_nombre(self, nombre: str):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre
    
    def set_cantidad_minima(self, cantidad: float):
        if cantidad < 0:
            raise ValueError("La cantidad mínima no puede ser negativa")
        self._cantidad_minima = cantidad
    
    def set_cantidad_maxima(self, cantidad: float):
        if cantidad < self._cantidad_minima:
            raise ValueError("La cantidad máxima no puede ser menor a la mínima")
        self._cantidad_maxima = cantidad
    
    def set_precio_unitario(self, precio: float):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio_unitario = precio
    
    def set_proveedor(self, proveedor: str):
        self._proveedor = proveedor
    
    def set_fecha_vencimiento(self, fecha: datetime):
        self._fecha_vencimiento = fecha
    
    def set_ubicacion_almacen(self, ubicacion: str):
        self._ubicacion_almacen = ubicacion
    
    def set_requiere_refrigeracion(self, requiere: bool):
        self._requiere_refrigeracion = requiere
    
    def set_notas(self, notas: str):
        self._notas = notas
    
    # --- GESTIÓN DE STOCK ---
    def agregar_stock(self, cantidad: float):
            """Agrega stock al ingrediente"""
            if cantidad <= 0:
                raise ValueError("La cantidad a agregar debe ser positiva")
            
            self._cantidad_actual += cantidad
            self._fecha_ultimo_reabastecimiento = datetime.now()
            
            self.notificar()
    
    def consumir_stock(self, cantidad: float):
        """Consume stock del ingrediente"""
        if cantidad <= 0:
            raise ValueError("La cantidad a consumir debe ser positiva")
        
        if cantidad > self._cantidad_actual:
            raise ValueError(f"Stock insuficiente. Disponible: {self._cantidad_actual} {self._unidad_medida}")
        
        self._cantidad_actual -= cantidad
        
        self.notificar() #
    
    def esta_agotado(self) -> bool:
        """Verifica si el ingrediente está agotado"""
        return self._cantidad_actual == 0
    
    def necesita_reabastecimiento(self) -> bool:
        """Verifica si el stock está por debajo del mínimo"""
        return self._cantidad_actual <= self._cantidad_minima
    
    def esta_en_stock_critico(self) -> bool:
        """Verifica si el stock está en nivel crítico"""
        return self._cantidad_actual <= STOCK_CRITICO
    
    def calcular_porcentaje_stock(self) -> float:
        """Calcula el porcentaje de stock actual respecto al máximo"""
        if self._cantidad_maxima == 0:
            return 0.0
        return (self._cantidad_actual / self._cantidad_maxima) * 100
    
    def calcular_cantidad_sugerida_reabastecimiento(self) -> float:
        """Calcula la cantidad sugerida para reabastecer hasta el máximo"""
        return max(0, self._cantidad_maxima - self._cantidad_actual)
    
    # --- VENCIMIENTO ---
    def esta_vencido(self) -> bool:
        """Verifica si el ingrediente está vencido"""
        if not self._fecha_vencimiento:
            return False
        return datetime.now() > self._fecha_vencimiento
    
    def esta_por_vencer(self) -> bool:
        """Verifica si el ingrediente está por vencer"""
        if not self._fecha_vencimiento:
            return False
        dias_restantes = (self._fecha_vencimiento - datetime.now()).days
        return 0 < dias_restantes <= DIAS_VENCIMIENTO_ALERTA
    
    def dias_hasta_vencimiento(self) -> Optional[int]:
        """Retorna los días hasta el vencimiento"""
        if not self._fecha_vencimiento:
            return None
        delta = self._fecha_vencimiento - datetime.now()
        return max(0, delta.days)
    
    # --- COSTOS ---
    def calcular_valor_stock(self) -> float:
        """Calcula el valor total del stock actual"""
        return self._cantidad_actual * self._precio_unitario
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        # Estado del stock
        if self.esta_agotado():
            estado_stock = "🔴 AGOTADO"
        elif self.esta_en_stock_critico():
            estado_stock = "🟠 CRÍTICO"
        elif self.necesita_reabastecimiento():
            estado_stock = "🟡 BAJO"
        else:
            estado_stock = "🟢 OK"
        
        # Vencimiento
        vencimiento_str = ""
        if self._fecha_vencimiento:
            if self.esta_vencido():
                vencimiento_str = f"\n  ⚠️ VENCIDO: {self._fecha_vencimiento.strftime('%d/%m/%Y')}"
            elif self.esta_por_vencer():
                dias = self.dias_hasta_vencimiento()
                vencimiento_str = f"\n  ⏰ Vence en {dias} días"
        
        # Refrigeración
        refrig = " ❄️" if self._requiere_refrigeracion else ""
        
        return (f"📦 {self._nombre}{refrig}\n"
                f"  Categoría: {self._categoria.value}\n"
                f"  Stock: {self._cantidad_actual:.2f} {self._unidad_medida} - {estado_stock}\n"
                f"  Mínimo: {self._cantidad_minima} | Máximo: {self._cantidad_maxima}\n"
                f"  Precio unitario: ${self._precio_unitario:.2f}\n"
                f"  Valor total: ${self.calcular_valor_stock():.2f}\n"
                f"  Proveedor: {self._proveedor if self._proveedor else 'N/A'}"
                f"{vencimiento_str}")
    
    def __repr__(self) -> str:
        return (f"Ingrediente(id={self._id}, "
                f"nombre='{self._nombre}', "
                f"stock={self._cantidad_actual}{self._unidad_medida})")

# ================================================================================
# ARCHIVO 5/5: unidad_medida.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/inventario/unidad_medida.py
# ================================================================================

from enum import Enum

class UnidadMedida(Enum):
    """Unidades de medida para ingredientes"""
    KILOGRAMOS = ("kg", "Kilogramos")
    GRAMOS = ("g", "Gramos")
    LITROS = ("L", "Litros")
    MILILITROS = ("mL", "Mililitros")
    UNIDADES = ("u", "Unidades")
    PORCIONES = ("porc", "Porciones")
    PAQUETES = ("paq", "Paquetes")
    
    def __init__(self, abreviatura: str, nombre_completo: str):
        self._abreviatura = abreviatura
        self._nombre_completo = nombre_completo
    
    @property
    def abreviatura(self) -> str:
        return self._abreviatura
    
    @property
    def nombre_completo(self) -> str:
        return self._nombre_completo
    
    def __str__(self):
        return self._abreviatura
    
    @classmethod
    def obtener_por_abreviatura(cls, abrev: str):
        """Busca una unidad por su abreviatura"""
        for unidad in cls:
            if unidad.abreviatura == abrev:
                return unidad
        return None

