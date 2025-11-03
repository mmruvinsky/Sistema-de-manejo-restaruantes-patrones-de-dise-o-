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