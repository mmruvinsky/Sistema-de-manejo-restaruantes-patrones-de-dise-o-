"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: bebida.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/bebida.py
# ================================================================================

from src.entidades.menu.item_menu import ItemMenu
from src.constantes import (
    PRECIO_BASE_BEBIDA, 
    TIEMPO_PREPARACION_BEBIDA,
    VINOS_MENDOCINOS,
    VINOS_SANJUANINOS
)

class Bebida(ItemMenu):
    """Bebidas del menú"""
    
    def __init__(self, nombre: str, descripcion: str, 
                 tipo_bebida: str, tamanio: str = "mediano"):
        super().__init__(
            nombre=nombre,
            descripcion=descripcion,
            precio_base=PRECIO_BASE_BEBIDA,
            tiempo_preparacion=TIEMPO_PREPARACION_BEBIDA
        )
        self._tipo_bebida = tipo_bebida  # "gaseosa", "jugo", "vino", "cerveza", "agua"
        self._tamanio = tamanio  # "chico", "mediano", "grande"
        self._es_alcoholica = False
        self._con_hielo = True
        self._origen_vino = None  # "mendocino" o "sanjuanino"
    
    def calcular_precio_final(self) -> float:
        """Precio base según tamaño, tipo y vinos específicos"""
        
        # Si es un vino mendocino o sanjuanino, usar precio específico
        if self._nombre in VINOS_MENDOCINOS:
            self._origen_vino = "mendocino"
            return VINOS_MENDOCINOS[self._nombre]
        
        if self._nombre in VINOS_SANJUANINOS:
            self._origen_vino = "sanjuanino"
            return VINOS_SANJUANINOS[self._nombre]
        
        # Para otras bebidas, usar lógica estándar
        precio = self._precio_base
        
        # Ajuste por tamaño
        if self._tamanio == "chico":
            precio *= 0.7
        elif self._tamanio == "grande":
            precio *= 1.5
        
        # Recargo por bebidas alcohólicas (cervezas, otros)
        if self._es_alcoholica:
            precio += 4.00
        
        return precio
    
    def get_estacion_cocina(self) -> str:
        """Todas las bebidas van a la barra"""
        return "Bebidas"
    
    def set_alcoholica(self, es_alcoholica: bool):
        self._es_alcoholica = es_alcoholica
    
    def es_alcoholica(self) -> bool:
        return self._es_alcoholica
    
    def set_con_hielo(self, con_hielo: bool):
        self._con_hielo = con_hielo
    
    def get_tamanio(self) -> str:
        return self._tamanio
    
    def get_origen_vino(self) -> str:
        """Retorna 'mendocino', 'sanjuanino' o None"""
        return self._origen_vino
    
    def es_vino_regional(self) -> bool:
        """Verifica si es un vino de la región (Mendoza o San Juan)"""
        return self._origen_vino is not None
    
    def __str__(self) -> str:
        base_str = super().__str__()
        
        # Agregar información de origen si es vino regional
        if self._origen_vino:
            origen_emoji = "🍷"
            origen_texto = f"\n  {origen_emoji} Vino {self._origen_vino.capitalize()}"
            return base_str + origen_texto
        
        return base_str

# ================================================================================
# ARCHIVO 3/8: categoria_item.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/categoria_item.py
# ================================================================================

from enum import Enum

class CategoriaItem(Enum):
    ENTRADA = "Entrada"
    PLATO_PRINCIPAL = "Plato Principal"
    POSTRE = "Postre"
    BEBIDA = "Bebida"
    OTRO = "Otro"

    def __str__(self):
        return self.value

# ================================================================================
# ARCHIVO 4/8: entrada.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/entrada.py
# ================================================================================

from src.entidades.menu.item_menu import ItemMenu
from src.constantes import PRECIO_BASE_ENTRADA, TIEMPO_PREPARACION_ENTRADA

class Entrada(ItemMenu):
    """Entradas/Aperitivos del menú"""
    
    def __init__(self, nombre: str, descripcion: str, tipo_entrada: str):
        super().__init__(
            nombre=nombre,
            descripcion=descripcion,
            precio_base=PRECIO_BASE_ENTRADA,
            tiempo_preparacion=TIEMPO_PREPARACION_ENTRADA
        )
        self._tipo_entrada = tipo_entrada  # "ensalada", "sopa", "tabla", etc.
    
    def calcular_precio_final(self) -> float:
        """Precio base sin modificaciones"""
        return self._precio_base
    
    def get_estacion_cocina(self) -> str:
        """Todas las entradas se preparan en la estación de cocina general"""
        return "Cocina"
    
    def get_tipo_entrada(self) -> str:
        return self._tipo_entrada

# ================================================================================
# ARCHIVO 5/8: item_menu.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/item_menu.py
# ================================================================================

from abc import ABC, abstractmethod
from typing import List, Dict

class ItemMenu(ABC):
    """Clase base abstracta para todos los items del menú"""
    
    _contador_id = 0
    
    def __init__(self, nombre: str, descripcion: str, precio_base: float, # en pesos argentinos
                 tiempo_preparacion: int):
        ItemMenu._contador_id += 1
        self._id = ItemMenu._contador_id
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio_base = precio_base
        self._tiempo_preparacion = tiempo_preparacion  # en minutos
        self._ingredientes: Dict[str, float] = {}  # {nombre_ingrediente: cantidad/peso
        self._disponible = True
        self._imagen_url = ""
        self._vegetariano = False
        self._vegano = False
        self._sin_gluten = False
    
    # Getters
    def get_id(self) -> int:
        return self._id
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_descripcion(self) -> str:
        return self._descripcion
    
    def get_precio_base(self) -> float:
        return self._precio_base
    
    def get_tiempo_preparacion(self) -> int:
        return self._tiempo_preparacion
    
    def get_ingredientes(self) -> Dict[str, float]:
        return self._ingredientes.copy()  # Defensive copy
    
    def esta_disponible(self) -> bool:
        return self._disponible
    
    def es_vegetariano(self) -> bool:
        return self._vegetariano
    
    def es_vegano(self) -> bool:
        return self._vegano
    
    def es_sin_gluten(self) -> bool:
        return self._sin_gluten
    
    # Setters
    def set_disponible(self, disponible: bool):
        self._disponible = disponible
    
    def set_precio_base(self, precio: float):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        self._precio_base = precio
    
    def agregar_ingrediente(self, nombre_ingrediente: str, cantidad: float):
        """Agrega un ingrediente necesario para este item"""
        self._ingredientes[nombre_ingrediente] = cantidad
    
    def set_vegetariano(self, es_vegetariano: bool):
        self._vegetariano = es_vegetariano
    
    def set_vegano(self, es_vegano: bool):
        self._vegano = es_vegano
        if es_vegano:
            self._vegetariano = True  # Vegano implica vegetariano
    
    def set_sin_gluten(self, sin_gluten: bool):
        self._sin_gluten = sin_gluten
    
    @abstractmethod
    def calcular_precio_final(self) -> float:
        """Cada tipo de item puede tener lógica de precio diferente"""
        pass
    
    @abstractmethod
    def get_estacion_cocina(self) -> str:
        """Define qué estación de cocina prepara este item"""
        pass
    
    def __str__(self) -> str:
        etiquetas = []
        if self._vegetariano:
            etiquetas.append("🌱 Vegetariano")
        if self._vegano:
            etiquetas.append("🥬 Vegano")
        if self._sin_gluten:
            etiquetas.append("🌾 Sin Gluten")
        
        etiquetas_str = " | ".join(etiquetas) if etiquetas else ""
        
        return (f"{self._nombre} - ${self.calcular_precio_final():.2f}\n"
                f"  {self._descripcion}\n"
                f"  {etiquetas_str}\n"
                f"  Tiempo de preparación: {self._tiempo_preparacion} min")

# ================================================================================
# ARCHIVO 6/8: plato_principal.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/plato_principal.py
# ================================================================================

# src/entidades/menu/plato_principal.py

from src.entidades.menu.item_menu import ItemMenu
from src.constantes import PRECIO_BASE_PLATO_PRINCIPAL, TIEMPO_PREPARACION_PLATO_PRINCIPAL

class PlatoPrincipal(ItemMenu):
    """Platos principales del menú"""
    
    def __init__(self, nombre: str, descripcion: str, 
                 tipo_proteina: str, guarnicion: str):
        super().__init__(
            nombre=nombre,
            descripcion=descripcion,
            precio_base=PRECIO_BASE_PLATO_PRINCIPAL,
            tiempo_preparacion=TIEMPO_PREPARACION_PLATO_PRINCIPAL
        )
        self._tipo_proteina = tipo_proteina  # "carne", "pollo", "pescado", "vegetariano"
        self._guarnicion = guarnicion  # "papas fritas", "ensalada", "arroz"
        self._punto_coccion = "medio"  # Para carnes
        self._salsa = None

        if self._tipo_proteina == "carne":
            self._punto_coccion = "medio"
    
    def calcular_precio_final(self) -> float:
        """Precio base + extras por tipo de proteína"""
        precio = self._precio_base
        
        # Recargo por tipo de proteína
        if self._tipo_proteina == "pescado":
            precio += 5.00
        elif self._tipo_proteina == "carne":
            precio += 4.00
        elif self._tipo_proteina == "pollo":
            precio += 3.00
        
        # Recargo por salsa premium
        if self._salsa and "premium" in self._salsa.lower():
            precio += 2.00
        
        return precio
    
    def get_estacion_cocina(self) -> str:
        """Define qué estación prepara este plato"""
        if self._tipo_proteina in ["carne", "pollo"]:
            return "Parrilla"
        
        elif self._tipo_proteina == "pescado":
            return "Cocina" # Antes decía "Plancha"
        
        else:
            # Asumimos que "vegetariano" va a Pastas o Cocina
            # Si "vegetariano" es el único 'else', va a Pastas.
            # Si quieres que vaya a Cocina General, cambia esto:
            if self._tipo_proteina == "vegetariano":
                 return "Cocina" # O "Pastas" si prefieres
            return "Pastas"  
    
    def set_punto_coccion(self, punto: str):
        PUNTOS_COCCION_CARNE = ["bleu", "jugoso", "a_punto", "bien_cocido"]
        if self._tipo_proteina != "carne":
            raise ValueError("El punto de cocción solo aplica para carnes")
        if punto not in PUNTOS_COCCION_CARNE:
            raise ValueError(f"Punto debe ser uno de: {PUNTOS_COCCION_CARNE}")
        self._punto_coccion = punto
    
    def get_punto_coccion(self) -> str:
        return self._punto_coccion
    
    def set_salsa(self, salsa: str):
        self._salsa = salsa
    
    def get_tipo_proteina(self) -> str:
        return self._tipo_proteina
    
    def get_guarnicion(self) -> str:
        return self._guarnicion

# ================================================================================
# ARCHIVO 7/8: postre.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/postre.py
# ================================================================================

from src.entidades.menu.item_menu import ItemMenu
from src.constantes import PRECIO_BASE_POSTRE, TIEMPO_PREPARACION_POSTRE

class Postre(ItemMenu):
    """Postres del menú"""
    
    def __init__(self, nombre: str, descripcion: str, 
                 tipo_postre: str, temperatura: str):
        super().__init__(
            nombre=nombre,
            descripcion=descripcion,
            precio_base=PRECIO_BASE_POSTRE,
            tiempo_preparacion=TIEMPO_PREPARACION_POSTRE
        )
        self._tipo_postre = tipo_postre  # "torta", "helado", "flan", etc.
        self._temperatura = temperatura  # "frío", "caliente"
        self._contiene_alcohol = False
    
    def calcular_precio_final(self) -> float:
        """Precio base + recargo por alcohol"""
        precio = self._precio_base
        
        if self._contiene_alcohol:
            precio += 3.00
        
        return precio
    
    def get_estacion_cocina(self) -> str:
        """Todos los postres van a la estación de postres"""
        return "Postres"
    
    def set_contiene_alcohol(self, contiene: bool):
        self._contiene_alcohol = contiene
    
    def contiene_alcohol(self) -> bool:
        return self._contiene_alcohol
    
    def get_tipo_postre(self) -> str:
        return self._tipo_postre
    
    def get_temperatura(self) -> str:
        return self._temperatura

# ================================================================================
# ARCHIVO 8/8: tipo_coccion.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/menu/tipo_coccion.py
# ================================================================================

from enum import Enum

class TipoCoccion(Enum):
    """Métodos de cocción disponibles en el restaurante"""
    PARRILLA = "Parrilla"
    PLANCHA = "Plancha"
    HORNO = "Horno"
    FRITURA = "Fritura"
    VAPOR = "Vapor"
    HERVIDO = "Hervido"
    CRUDO = "Crudo"  # Para ensaladas, ceviches, etc.
    
    @classmethod
    def valores_validos(cls):
        """Retorna lista de valores válidos"""
        return [e.value for e in cls]
    
    def __str__(self):
        return self.value

