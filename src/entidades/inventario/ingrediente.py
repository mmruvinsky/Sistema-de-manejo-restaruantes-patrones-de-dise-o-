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