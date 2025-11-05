from typing import Dict, List, Optional
from datetime import datetime
from src.entidades.salon.reserva import Reserva
from src.entidades.salon.estado_reserva import EstadoReserva
from src.servicios.salon.mesa_service import MesaService

class ReservaService:
    """
    Servicio Singleton para gestionar las reservas.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._reservas: Dict[int, Reserva] = {}
        self._mesa_service = MesaService() # Usa el servicio de mesas
        self._inicializado = True
        print("Servicio de Reservas inicializado.")
        
    def crear_reserva(self, cliente_id: int, fecha_hora: datetime, 
                      cantidad: int, nombre: str, telefono: str) -> Reserva:
        
        # 1. Buscar si hay mesa disponible para esa hora
        # (Aquí iría una lógica compleja de disponibilidad vs. reservas existentes)
        
        # 2. Si hay, buscar una mesa adecuada
        mesa = self._mesa_service.buscar_mesa_disponible(cantidad) # Simplificación
        
        if not mesa:
            raise ValueError("No hay mesas disponibles para esa cantidad de personas")
            
        # 3. Crear la reserva
        reserva = Reserva(cliente_id, fecha_hora, cantidad, nombre, telefono)
        
        # 4. Asignar y reservar la mesa
        reserva.set_mesa_asignada(mesa.get_id())
        mesa.reservar(reserva.get_id())
        
        self._reservas[reserva.get_id()] = reserva
        print(f"Reserva #{reserva.get_id()} creada para Mesa #{mesa.get_numero()}")
        return reserva

    def get_reserva(self, reserva_id: int) -> Optional[Reserva]:
        return self._reservas.get(reserva_id)
        
    def confirmar_llegada(self, reserva_id: int):
        reserva = self.get_reserva(reserva_id)
        if not reserva:
            raise ValueError("Reserva no encontrada")
            
        reserva.registrar_llegada()
        
        # Ocupar la mesa
        mesa_id = reserva.get_mesa_asignada_id()
        if mesa_id:
            mesa = self._mesa_service.get_mesa(mesa_id)
            if mesa and mesa.esta_reservada():
                # Asumimos que se crea un pedido en este momento
                # (Lógica de PedidoService iría aquí)
                pedido_id_nuevo = 999 # ID de pedido simulado
                
                mesa.ocupar(reserva.get_cantidad_personas(), pedido_id_nuevo)
                print(f"Reserva #{reserva_id} registrada. Mesa #{mesa.get_numero()} ocupada.")
            else:
                print(f"Advertencia: Mesa #{mesa_id} no estaba en estado 'Reservada'.")