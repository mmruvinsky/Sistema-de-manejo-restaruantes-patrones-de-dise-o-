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