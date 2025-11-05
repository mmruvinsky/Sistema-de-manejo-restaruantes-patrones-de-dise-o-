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