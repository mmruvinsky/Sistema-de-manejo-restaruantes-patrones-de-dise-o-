from abc import ABC, abstractmethod
from typing import List, Optional
from datetime import datetime
from src.entidades.cocina.orden_cocina import OrdenCocina
from src.entidades.cocina.estado_orden import EstadoOrden


class EstacionCocina(ABC):
    """Clase base abstracta para todas las estaciones de cocina"""
    
    def __init__(self, nombre_estacion: str, capacidad_maxima: int):
        self._nombre_estacion = nombre_estacion
        self._capacidad_maxima = capacidad_maxima  # Órdenes simultáneas
        self._ordenes_pendientes: List[OrdenCocina] = []
        self._ordenes_en_preparacion: List[OrdenCocina] = []
        self._ordenes_completadas: List[OrdenCocina] = []
        self._activa = True
        self._temperatura_actual = 20.0  # °C
        self._chef_responsable_id: Optional[int] = None
    
    # --- GETTERS ---
    def get_nombre_estacion(self) -> str:
        return self._nombre_estacion
    
    def get_capacidad_maxima(self) -> int:
        return self._capacidad_maxima
    
    def get_ordenes_pendientes(self) -> List[OrdenCocina]:
        return self._ordenes_pendientes.copy()
    
    def get_ordenes_en_preparacion(self) -> List[OrdenCocina]:
        return self._ordenes_en_preparacion.copy()
    
    def get_ordenes_completadas(self) -> List[OrdenCocina]:
        return self._ordenes_completadas.copy()
    
    def esta_activa(self) -> bool:
        return self._activa
    
    def get_temperatura_actual(self) -> float:
        return self._temperatura_actual
    
    def get_chef_responsable_id(self) -> Optional[int]:
        return self._chef_responsable_id
    
    # --- SETTERS ---
    def set_activa(self, activa: bool):
        self._activa = activa
    
    def set_temperatura_actual(self, temperatura: float):
        self._temperatura_actual = temperatura
    
    def set_chef_responsable(self, chef_id: int):
        self._chef_responsable_id = chef_id
    
    # --- GESTIÓN DE ÓRDENES ---
    def recibir_orden(self, orden: OrdenCocina):
        """Recibe una nueva orden en la estación"""
        if not self._activa:
            raise ValueError(f"La estación {self._nombre_estacion} no está activa")
        
        if orden.get_estacion_asignada() != self._nombre_estacion:
            raise ValueError(f"Esta orden no pertenece a la estación {self._nombre_estacion}")
        
        self._ordenes_pendientes.append(orden)
        self._ordenes_pendientes.sort(key=lambda o: (-o.get_prioridad(), o.get_id()))
    
    def iniciar_orden(self, orden_id: int) -> bool:
        """Inicia la preparación de una orden pendiente"""
        if not self.puede_iniciar_orden():
            return False
        
        for i, orden in enumerate(self._ordenes_pendientes):
            if orden.get_id() == orden_id:
                orden.iniciar_preparacion()
                self._ordenes_en_preparacion.append(orden)
                self._ordenes_pendientes.pop(i)
                return True
        return False
    
    def completar_orden(self, orden_id: int):
        """Marca una orden como completada"""
        for i, orden in enumerate(self._ordenes_en_preparacion):
            if orden.get_id() == orden_id:
                orden.marcar_como_lista()
                self._ordenes_completadas.append(orden)
                self._ordenes_en_preparacion.pop(i)
                return True
        return False
    
    def cancelar_orden(self, orden_id: int, motivo: str = ""):
        """Cancela una orden"""
        # Buscar en pendientes
        for i, orden in enumerate(self._ordenes_pendientes):
            if orden.get_id() == orden_id:
                orden.cancelar(motivo)
                self._ordenes_pendientes.pop(i)
                return True
        
        # Buscar en preparación
        for i, orden in enumerate(self._ordenes_en_preparacion):
            if orden.get_id() == orden_id:
                orden.cancelar(motivo)
                self._ordenes_en_preparacion.pop(i)
                return True
        
        return False
    
    # --- VALIDACIONES ---
    def puede_iniciar_orden(self) -> bool:
        """Verifica si hay capacidad para iniciar otra orden"""
        return len(self._ordenes_en_preparacion) < self._capacidad_maxima
    
    def tiene_ordenes_pendientes(self) -> bool:
        """Verifica si hay órdenes pendientes"""
        return len(self._ordenes_pendientes) > 0
    
    def esta_saturada(self) -> bool:
        """Verifica si la estación está a máxima capacidad"""
        return len(self._ordenes_en_preparacion) >= self._capacidad_maxima
    
    # --- ESTADÍSTICAS ---
    def contar_ordenes_totales(self) -> int:
        """Cuenta todas las órdenes en la estación"""
        return (len(self._ordenes_pendientes) + 
                len(self._ordenes_en_preparacion) + 
                len(self._ordenes_completadas))
    
    def calcular_tiempo_promedio_preparacion(self) -> float:
        """Calcula el tiempo promedio de preparación de órdenes completadas"""
        if not self._ordenes_completadas:
            return 0.0
        
        tiempos = [o.calcular_tiempo_preparacion() 
                   for o in self._ordenes_completadas 
                   if o.calcular_tiempo_preparacion() is not None]
        
        if not tiempos:
            return 0.0
        
        return sum(tiempos) / len(tiempos)
    
    def obtener_ordenes_retrasadas(self) -> List[OrdenCocina]:
        """Retorna lista de órdenes retrasadas"""
        return [o for o in self._ordenes_en_preparacion if o.esta_retrasada()]
    
    def limpiar_ordenes_completadas(self):
        """Limpia las órdenes completadas (para mantenimiento)"""
        self._ordenes_completadas.clear()
    
    # --- MÉTODOS ABSTRACTOS ---
    @abstractmethod
    def verificar_equipamiento(self) -> bool:
        """Verifica que el equipamiento esté funcionando correctamente"""
        pass
    
    @abstractmethod
    def realizar_mantenimiento(self):
        """Realiza tareas de mantenimiento específicas de la estación"""
        pass
    
    @abstractmethod
    def obtener_temperatura_operacion(self) -> tuple:
        """Retorna (temp_minima, temp_maxima) de operación"""
        pass
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado = "✅ Activa" if self._activa else "❌ Inactiva"
        saturacion = "🔴 SATURADA" if self.esta_saturada() else "🟢 OK"
        
        retrasadas = self.obtener_ordenes_retrasadas()
        alerta_retrasos = f"\n  ⚠️ {len(retrasadas)} órdenes retrasadas" if retrasadas else ""
        
        return (f"🏭 Estación: {self._nombre_estacion}\n"
                f"  Estado: {estado} - {saturacion}\n"
                f"  Capacidad: {len(self._ordenes_en_preparacion)}/{self._capacidad_maxima}\n"
                f"  Pendientes: {len(self._ordenes_pendientes)}\n"
                f"  En preparación: {len(self._ordenes_en_preparacion)}\n"
                f"  Completadas (hoy): {len(self._ordenes_completadas)}\n"
                f"  Temperatura: {self._temperatura_actual}°C\n"
                f"  Tiempo promedio: {self.calcular_tiempo_promedio_preparacion():.1f} min"
                f"{alerta_retrasos}")
    
    def __repr__(self) -> str:
        return f"EstacionCocina(nombre='{self._nombre_estacion}', ordenes={self.contar_ordenes_totales()})"