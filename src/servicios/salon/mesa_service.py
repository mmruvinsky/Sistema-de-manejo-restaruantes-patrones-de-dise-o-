from typing import Dict, List, Optional
from src.entidades.salon.mesa import Mesa
from src.entidades.salon.estado_mesa import EstadoMesa

class MesaService:
    """
    Servicio Singleton para gestionar las mesas del salón.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._mesas: Dict[int, Mesa] = {} # Por ID de mesa
        self._inicializado = True
        print("Servicio de Mesas inicializado.")
        
    def agregar_mesa(self, mesa: Mesa):
        if mesa.get_id() not in self._mesas:
            self._mesas[mesa.get_id()] = mesa

    def get_mesa(self, mesa_id: int) -> Optional[Mesa]:
        return self._mesas.get(mesa_id)
        
    def get_mesas_por_estado(self, estado: EstadoMesa) -> List[Mesa]:
        return [m for m in self._mesas.values() if m.get_estado() == estado]
        
    def buscar_mesa_disponible(self, cantidad_personas: int) -> Optional[Mesa]:
        disponibles = self.get_mesas_por_estado(EstadoMesa.DISPONIBLE)
        # Ordenar por capacidad (la más ajustada primero)
        disponibles.sort(key=lambda m: m.get_capacidad())
        
        for mesa in disponibles:
            if mesa.puede_aceptar_comensales(cantidad_personas):
                return mesa
        return None # No hay mesas disponibles

    def ocupar_mesa(self, mesa_id: int, cantidad: int, pedido_id: int):
        mesa = self.get_mesa(mesa_id)
        if mesa:
            mesa.ocupar(cantidad, pedido_id)
            print(f"Mesa #{mesa.get_numero()} ocupada.")
        
    def liberar_mesa(self, mesa_id: int):
        mesa = self.get_mesa(mesa_id)
        if mesa:
            mesa.liberar()
            print(f"Mesa #{mesa.get_numero()} liberada (en limpieza).")