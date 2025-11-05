from src.entidades.menu.item_menu import ItemMenu

class ItemPedido:
    """Representa un item individual dentro de un pedido con su cantidad"""
    
    _contador_id = 0
    
    def __init__(self, item_menu: ItemMenu, cantidad: int = 1):
        ItemPedido._contador_id += 1
        self._id = ItemPedido._contador_id
        self._item_menu = item_menu
        self._cantidad = cantidad
        self._observaciones_especiales = ""
        self._precio_unitario_congelado = None  # Para guardar precio al momento del pedido
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_item_menu(self) -> ItemMenu:
        return self._item_menu
    
    def get_cantidad(self) -> int:
        return self._cantidad
    
    def get_observaciones_especiales(self) -> str:
        return self._observaciones_especiales
    
    def get_precio_unitario(self) -> float:
        """Retorna el precio unitario (congelado o actual)"""
        if self._precio_unitario_congelado is not None:
            return self._precio_unitario_congelado
        return self._item_menu.calcular_precio_final()
    
    # --- SETTERS ---
    def set_cantidad(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        self._cantidad = cantidad
    
    def set_observaciones_especiales(self, observaciones: str):
        """Ej: 'sin cebolla', 'bien cocido', 'sin hielo'"""
        self._observaciones_especiales = observaciones
    
    def congelar_precio(self):
        """Congela el precio actual para que no cambie si el menú se actualiza"""
        self._precio_unitario_congelado = self._item_menu.calcular_precio_final()
    
    # --- OPERACIONES ---
    def aumentar_cantidad(self, incremento: int = 1):
        """Aumenta la cantidad del item"""
        if incremento <= 0:
            raise ValueError("El incremento debe ser positivo")
        self._cantidad += incremento
    
    def disminuir_cantidad(self, decremento: int = 1):
        """Disminuye la cantidad del item"""
        if decremento <= 0:
            raise ValueError("El decremento debe ser positivo")
        if self._cantidad - decremento < 1:
            raise ValueError("La cantidad no puede ser menor a 1")
        self._cantidad -= decremento
    
    # --- CÁLCULOS ---
    def calcular_precio_total(self) -> float:
        """Calcula el precio total (precio unitario * cantidad)"""
        return self.get_precio_unitario() * self._cantidad
    
    def calcular_tiempo_preparacion_total(self) -> int:
        """Retorna el tiempo de preparación (no se multiplica por cantidad)"""
        return self._item_menu.get_tiempo_preparacion()
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        obs = f" ({self._observaciones_especiales})" if self._observaciones_especiales else ""
        return (f"{self._cantidad}x {self._item_menu.get_nombre()} - "
                f"${self.calcular_precio_total():.2f}{obs}")
    
    def __repr__(self) -> str:
        return (f"ItemPedido(id={self._id}, "
                f"item={self._item_menu.get_nombre()}, "
                f"cantidad={self._cantidad})")