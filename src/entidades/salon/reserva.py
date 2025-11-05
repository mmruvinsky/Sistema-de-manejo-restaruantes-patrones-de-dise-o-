from typing import Optional
from datetime import datetime, timedelta
from src.entidades.salon.estado_reserva import EstadoReserva    

class Reserva:
    """Representa una reserva de mesa"""
    
    _contador_id = 0
    
    def __init__(self, cliente_id: int, fecha_hora: datetime, 
                 cantidad_personas: int, nombre_contacto: str, telefono_contacto: str):
        Reserva._contador_id += 1
        self._id = Reserva._contador_id
        self._cliente_id = cliente_id
        self._fecha_hora = fecha_hora
        self._cantidad_personas = cantidad_personas
        self._nombre_contacto = nombre_contacto
        self._telefono_contacto = telefono_contacto
        self._estado = EstadoReserva.PENDIENTE
        self._mesa_asignada_id: Optional[int] = None
        self._fecha_hora_creacion = datetime.now()
        self._fecha_hora_confirmacion: Optional[datetime] = None
        self._fecha_hora_llegada: Optional[datetime] = None
        self._observaciones = ""
        self._ocasion_especial = ""  # cumpleaños, aniversario, etc.
        self._tiempo_tolerancia = 15  # minutos
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_cliente_id(self) -> int:
        return self._cliente_id
    
    def get_fecha_hora(self) -> datetime:
        return self._fecha_hora
    
    def get_cantidad_personas(self) -> int:
        return self._cantidad_personas
    
    def get_nombre_contacto(self) -> str:
        return self._nombre_contacto
    
    def get_telefono_contacto(self) -> str:
        return self._telefono_contacto
    
    def get_estado(self) -> EstadoReserva:
        return self._estado
    
    def get_mesa_asignada_id(self) -> Optional[int]:
        return self._mesa_asignada_id
    
    def get_observaciones(self) -> str:
        return self._observaciones
    
    def get_ocasion_especial(self) -> str:
        return self._ocasion_especial
    
    # --- SETTERS ---
    def set_observaciones(self, observaciones: str):
        self._observaciones = observaciones
    
    def set_ocasion_especial(self, ocasion: str):
        """Ej: 'Cumpleaños', 'Aniversario', 'Cita romántica'"""
        self._ocasion_especial = ocasion
    
    def set_mesa_asignada(self, mesa_id: int):
        self._mesa_asignada_id = mesa_id
    
    def set_fecha_hora(self, nueva_fecha_hora: datetime):
        """Modifica la fecha/hora de la reserva"""
        if self._estado not in [EstadoReserva.PENDIENTE, EstadoReserva.CONFIRMADA]:
            raise ValueError("No se puede modificar una reserva en este estado")
        self._fecha_hora = nueva_fecha_hora
    
    def set_cantidad_personas(self, cantidad: int):
        """Modifica la cantidad de personas"""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        if self._estado not in [EstadoReserva.PENDIENTE, EstadoReserva.CONFIRMADA]:
            raise ValueError("No se puede modificar una reserva en este estado")
        self._cantidad_personas = cantidad
    
    # --- GESTIÓN DE ESTADO ---
    def confirmar(self):
        """Confirma la reserva"""
        if self._estado != EstadoReserva.PENDIENTE:
            raise ValueError("Solo se pueden confirmar reservas pendientes")
        self._estado = EstadoReserva.CONFIRMADA
        self._fecha_hora_confirmacion = datetime.now()
    
    def registrar_llegada(self):
        """Registra la llegada del cliente"""
        if self._estado != EstadoReserva.CONFIRMADA:
            raise ValueError("La reserva debe estar confirmada")
        self._estado = EstadoReserva.EN_CURSO
        self._fecha_hora_llegada = datetime.now()
    
    def completar(self):
        """Marca la reserva como completada"""
        if self._estado != EstadoReserva.EN_CURSO:
            raise ValueError("La reserva debe estar en curso")
        self._estado = EstadoReserva.COMPLETADA
    
    def cancelar(self, motivo: str = ""):
        """Cancela la reserva"""
        if self._estado in [EstadoReserva.COMPLETADA, EstadoReserva.NO_SHOW]:
            raise ValueError("No se puede cancelar una reserva completada o no show")
        self._estado = EstadoReserva.CANCELADA
        if motivo:
            self.set_observaciones(f"Cancelada: {motivo}")
    
    def marcar_no_show(self):
        """Marca como no presentado"""
        if self._estado != EstadoReserva.CONFIRMADA:
            raise ValueError("Solo se puede marcar no show reservas confirmadas")
        
        # Verificar que ya pasó la hora + tolerancia
        if not self.esta_vencida():
            raise ValueError("Aún no ha vencido el tiempo de tolerancia")
        
        self._estado = EstadoReserva.NO_SHOW
    
    # --- VALIDACIONES ---
    def esta_vigente(self) -> bool:
        """Verifica si la reserva está vigente (no cancelada, no vencida)"""
        if self._estado in [EstadoReserva.CANCELADA, EstadoReserva.NO_SHOW, EstadoReserva.COMPLETADA]:
            return False
        return not self.esta_vencida()
    
    def esta_vencida(self) -> bool:
        """Verifica si ya pasó la hora de la reserva + tolerancia"""
        hora_limite = self._fecha_hora + timedelta(minutes=self._tiempo_tolerancia)
        return datetime.now() > hora_limite
    
    def puede_cancelarse(self) -> bool:
        """Verifica si la reserva puede cancelarse"""
        return self._estado in [EstadoReserva.PENDIENTE, EstadoReserva.CONFIRMADA]
    
    def esta_proxima(self, minutos: int = 60) -> bool:
        """Verifica si la reserva está próxima (dentro de X minutos)"""
        if self._estado not in [EstadoReserva.CONFIRMADA]:
            return False
        delta = self._fecha_hora - datetime.now()
        return 0 <= delta.total_seconds() / 60 <= minutos
    
    # --- CÁLCULOS ---
    def calcular_tiempo_anticipacion(self) -> int:
        """Calcula con cuántos días de anticipación se hizo la reserva"""
        delta = self._fecha_hora - self._fecha_hora_creacion
        return delta.days
    
    def calcular_tiempo_hasta_reserva(self) -> Optional[int]:
        """Retorna minutos hasta la hora de la reserva (negativo si ya pasó)"""
        if self._estado not in [EstadoReserva.PENDIENTE, EstadoReserva.CONFIRMADA]:
            return None
        delta = self._fecha_hora - datetime.now()
        return int(delta.total_seconds() / 60)
    
    def calcular_retraso_llegada(self) -> Optional[int]:
        """Calcula el retraso en minutos respecto a la hora de reserva"""
        if not self._fecha_hora_llegada:
            return None
        delta = self._fecha_hora_llegada - self._fecha_hora
        return int(delta.total_seconds() / 60)
    
    # --- NOTIFICACIONES ---
    def necesita_recordatorio(self) -> bool:
        """Verifica si necesita enviar recordatorio (24hs antes)"""
        if self._estado != EstadoReserva.CONFIRMADA:
            return False
        
        tiempo_hasta = self.calcular_tiempo_hasta_reserva()
        if tiempo_hasta is None:
            return False
        
        # Recordatorio entre 24hs y 23hs antes
        return 1380 <= tiempo_hasta <= 1440  # minutos
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado_emoji = {
            EstadoReserva.PENDIENTE: "⏳",
            EstadoReserva.CONFIRMADA: "✅",
            EstadoReserva.EN_CURSO: "🍽️",
            EstadoReserva.COMPLETADA: "✔️",
            EstadoReserva.CANCELADA: "❌",
            EstadoReserva.NO_SHOW: "👻"
        }
        
        mesa_str = f"Mesa #{self._mesa_asignada_id}" if self._mesa_asignada_id else "Sin asignar"
        ocasion_str = f"\n  🎉 Ocasión: {self._ocasion_especial}" if self._ocasion_especial else ""
        obs_str = f"\n  📝 {self._observaciones}" if self._observaciones else ""
        
        tiempo_hasta = self.calcular_tiempo_hasta_reserva()
        tiempo_str = ""
        if tiempo_hasta is not None:
            if tiempo_hasta > 0:
                tiempo_str = f"\n  ⏰ Faltan {tiempo_hasta} minutos"
            elif tiempo_hasta < 0:
                tiempo_str = f"\n  ⚠️ Retrasada {abs(tiempo_hasta)} minutos"
        
        return (f"{estado_emoji.get(self._estado, '📅')} Reserva #{self._id}\n"
                f"  Estado: {self._estado.value}\n"
                f"  Contacto: {self._nombre_contacto} - {self._telefono_contacto}\n"
                f"  Fecha: {self._fecha_hora.strftime('%d/%m/%Y %H:%M')}\n"
                f"  Personas: {self._cantidad_personas}\n"
                f"  {mesa_str}"
                f"{ocasion_str}"
                f"{tiempo_str}"
                f"{obs_str}")
    
    def __repr__(self) -> str:
        return (f"Reserva(id={self._id}, "
                f"cliente={self._cliente_id}, "
                f"fecha={self._fecha_hora.strftime('%d/%m/%Y')}, "
                f"estado={self._estado})")