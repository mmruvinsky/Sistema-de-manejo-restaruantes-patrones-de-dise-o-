"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: estacion_bebidas.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/estacion_bebidas.py
# ================================================================================

from datetime import datetime
from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.entidades.cocina.orden_cocina import OrdenCocina

class EstacionBebidas(EstacionCocina):
    """Estación especializada en bebidas (barra)"""
    
    def __init__(self):
        super().__init__(nombre_estacion="Bebidas", capacidad_maxima=10)
        self._hielo_disponible_kg = 50.0
        self._copas_limpias = 100
        self._vasos_limpios = 150
        self._maquina_cafe_encendida = True
        self._ultima_limpieza = None
    
    # --- GETTERS ESPECÍFICOS ---
    def get_hielo_disponible(self) -> float:
        return self._hielo_disponible_kg
    
    def get_copas_limpias(self) -> int:
        return self._copas_limpias
    
    def get_vasos_limpios(self) -> int:
        return self._vasos_limpios
    
    def esta_maquina_cafe_encendida(self) -> bool:
        return self._maquina_cafe_encendida
    
    # --- OPERACIONES ---
    def agregar_hielo(self, cantidad_kg: float):
        """Agrega hielo"""
        if cantidad_kg <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self._hielo_disponible_kg += cantidad_kg
    
    def consumir_hielo(self, cantidad_kg: float = 0.2):
        """Consume hielo al preparar bebida"""
        if self._hielo_disponible_kg < cantidad_kg:
            raise ValueError("No hay suficiente hielo")
        self._hielo_disponible_kg -= cantidad_kg
    
    def usar_copa(self):
        """Usa una copa"""
        if self._copas_limpias <= 0:
            raise ValueError("No hay copas limpias")
        self._copas_limpias -= 1
    
    def usar_vaso(self):
        """Usa un vaso"""
        if self._vasos_limpios <= 0:
            raise ValueError("No hay vasos limpios")
        self._vasos_limpios -= 1
    
    def lavar_cristaleria(self, copas: int = 0, vasos: int = 0):
        """Agrega copas y vasos limpios"""
        self._copas_limpias += copas
        self._vasos_limpios += vasos
    
    # --- OVERRIDE DE MÉTODOS ABSTRACTOS ---
    def verificar_equipamiento(self) -> bool:
        """Verifica que se pueda preparar bebidas"""
        if not self._maquina_cafe_encendida:
            return False
        if self._hielo_disponible_kg < 1.0:
            return False
        if self._copas_limpias + self._vasos_limpios < 10:
            return False
        return True
    
    def realizar_mantenimiento(self):
        """Realiza limpieza de la barra"""
        self._ultima_limpieza = datetime.now()
        self.limpiar_ordenes_completadas()
    
    def obtener_temperatura_operacion(self) -> tuple:
        """Rango óptimo de temperatura"""
        return (18, 25)  # °C
    
    # --- VALIDACIONES ---
    def necesita_hielo(self) -> bool:
        """Verifica si necesita hielo"""
        return self._hielo_disponible_kg < 10.0
    
    def necesita_cristaleria(self) -> bool:
        """Verifica si necesita lavar cristalería"""
        return (self._copas_limpias < 20 or self._vasos_limpios < 30)
    
    def puede_preparar_bebidas(self) -> bool:
        """Verifica si puede preparar bebidas"""
        return (self._hielo_disponible_kg >= 0.2 and 
                (self._copas_limpias > 0 or self._vasos_limpios > 0))
    
    # --- OVERRIDE DE COMPLETAR ORDEN ---
    def completar_orden(self, orden_id: int):
        """Override para consumir recursos"""
        resultado = super().completar_orden(orden_id)
        if resultado:
            # Lógica simplificada: alternamos entre copa y vaso
            if self._copas_limpias > 0:
                self.usar_copa()
            else:
                self.usar_vaso()
            self.consumir_hielo(0.1)
        return resultado
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        
        hielo_alerta = "⚠️ BAJO" if self.necesita_hielo() else "✓"
        cristal_alerta = "⚠️ LAVAR" if self.necesita_cristaleria() else "✓"
        cafe = "☕ Encendida" if self._maquina_cafe_encendida else "☕ Apagada"
        
        return (f"{base_str}\n"
                f"  Máquina café: {cafe}\n"
                f"  Hielo: {self._hielo_disponible_kg:.1f} kg {hielo_alerta}\n"
                f"  Copas: {self._copas_limpias} | Vasos: {self._vasos_limpios} {cristal_alerta}")
    
    def __repr__(self) -> str:
        return f"EstacionBebidas(ordenes={self.contar_ordenes_totales()}, hielo={self._hielo_disponible_kg:.1f}kg)"

# ================================================================================
# ARCHIVO 3/9: estacion_cocina.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/estacion_cocina.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/9: estacion_cocina_general.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/estacion_cocina_general.py
# ================================================================================

# src/entidades/cocina/estacion_cocina_general.py

from datetime import datetime
from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.constantes import TEMPERATURA_COCINA_MIN, TEMPERATURA_COCINA_MAX

class EstacionCocinaGeneral(EstacionCocina):
    """
    Estación de cocina general para items que no tienen
    una estación especializada (ej. Entradas, Pescados).
    Implementación concreta de EstacionCocina.
    """
    
    def __init__(self):
        # Llama al init de la clase base con sus valores
        super().__init__(nombre_estacion="Cocina", capacidad_maxima=10)
        self._ultima_limpieza = None
        # Asumimos que la cocina general empieza encendida
        self.set_activa(True) 
        self.set_temperatura_actual(22.0) # Temperatura ambiente
    
    # --- Implementación de métodos abstractos ---
    
    def verificar_equipamiento(self) -> bool:
        """
        Implementación simple: Asume que la cocina general
        siempre está operativa si está activa y en temperatura.
        """
        temp_ok = (TEMPERATURA_COCINA_MIN <= 
                   self.get_temperatura_actual() <= 
                   TEMPERATURA_COCINA_MAX)
        
        if not temp_ok:
            print(f"ALERTA: Temperatura fuera de rango en {self.get_nombre_estacion()}")
            
        return self.esta_activa() and temp_ok
    
    def realizar_mantenimiento(self):
        """Implementación simple: solo limpia órdenes completadas."""
        print(f"Realizando mantenimiento en {self.get_nombre_estacion()}...")
        self._ultima_limpieza = datetime.now()
        self.limpiar_ordenes_completadas()
    
    def obtener_temperatura_operacion(self) -> tuple:
        """Retorna el rango estándar de temperatura ambiente de cocina."""
        return (TEMPERATURA_COCINA_MIN, TEMPERATURA_COCINA_MAX)

# ================================================================================
# ARCHIVO 5/9: estacion_parrilla.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/estacion_parrilla.py
# ================================================================================

from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.constantes import TEMPERATURA_PARRILLA


class EstacionParrilla(EstacionCocina):
    """Estación especializada en parrilla (carnes y pollo)"""
    
    def __init__(self):
        super().__init__(nombre_estacion="Parrilla", capacidad_maxima=8)
        self._temperatura_parrilla = TEMPERATURA_PARRILLA
        self._carbon_disponible = 100.0  # kg
        self._parrilla_encendida = False
        self._ultima_limpieza = None
    
    # --- GETTERS ESPECÍFICOS ---
    def get_temperatura_parrilla(self) -> float:
        return self._temperatura_parrilla
    
    def get_carbon_disponible(self) -> float:
        return self._carbon_disponible
    
    def esta_parrilla_encendida(self) -> bool:
        return self._parrilla_encendida
    
    # --- SETTERS ESPECÍFICOS ---
    def set_temperatura_parrilla(self, temperatura: float):
        if temperatura < 150 or temperatura > 300:
            raise ValueError("Temperatura de parrilla fuera de rango (150-300°C)")
        self._temperatura_parrilla = temperatura
    
    def encender_parrilla(self):
        """Enciende la parrilla"""
        if self._carbon_disponible < 5:
            raise ValueError("No hay suficiente carbón para encender la parrilla")
        self._parrilla_encendida = True
        self._temperatura_parrilla = TEMPERATURA_PARRILLA
    
    def apagar_parrilla(self):
        """Apaga la parrilla"""
        self._parrilla_encendida = False
        self._temperatura_parrilla = self._temperatura_actual
    
    def agregar_carbon(self, cantidad: float):
        """Agrega carbón a la parrilla"""
        if cantidad <= 0:
            raise ValueError("La cantidad de carbón debe ser positiva")
        self._carbon_disponible += cantidad
    
    def consumir_carbon(self, cantidad: float = 2.0):
        """Consume carbón durante la cocción"""
        if self._carbon_disponible < cantidad:
            raise ValueError("No hay suficiente carbón")
        self._carbon_disponible -= cantidad
    
    # --- OVERRIDE DE MÉTODOS ABSTRACTOS ---
    def verificar_equipamiento(self) -> bool:
        """Verifica que la parrilla esté en condiciones de operar"""
        if not self._parrilla_encendida:
            return False
        
        if self._carbon_disponible < 10:
            return False
        
        if self._temperatura_parrilla < 150:
            return False
        
        return True
    
    def realizar_mantenimiento(self):
        """Realiza limpieza y mantenimiento de la parrilla"""
        from datetime import datetime
        self._ultima_limpieza = datetime.now()
        # Limpiar órdenes completadas
        self.limpiar_ordenes_completadas()
    
    def obtener_temperatura_operacion(self) -> tuple:
        """Retorna rango de temperatura óptima de operación"""
        return (180, 220)  # °C
    
    # --- MÉTODOS ESPECÍFICOS ---
    def puede_cocinar_a_la_parrilla(self) -> bool:
        """Verifica si se puede cocinar (parrilla encendida y con carbón)"""
        return (self._parrilla_encendida and 
                self._carbon_disponible >= 5 and 
                self._temperatura_parrilla >= 150)
    
    def necesita_carbon(self) -> bool:
        """Verifica si necesita reposición de carbón"""
        return self._carbon_disponible < 20
    
    def ajustar_temperatura(self, incremento: float):
        """Ajusta la temperatura de la parrilla"""
        nueva_temp = self._temperatura_parrilla + incremento
        self.set_temperatura_parrilla(nueva_temp)
    
    # --- OVERRIDE DE RECIBIR ORDEN ---
    def recibir_orden(self, orden):
        """Override para verificar que la parrilla esté lista"""
        if not self.puede_cocinar_a_la_parrilla():
            raise ValueError("La parrilla no está lista para cocinar")
        super().recibir_orden(orden)
    
    # --- OVERRIDE DE COMPLETAR ORDEN ---
    def completar_orden(self, orden_id: int):
        """Override para consumir carbón al completar"""
        resultado = super().completar_orden(orden_id)
        if resultado:
            self.consumir_carbon(1.5)  # Consume carbón por orden
        return resultado
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        
        parrilla_estado = "🔥 Encendida" if self._parrilla_encendida else "⚫ Apagada"
        carbon_alerta = "⚠️ BAJO" if self.necesita_carbon() else "✓"
        
        return (f"{base_str}\n"
                f"  Parrilla: {parrilla_estado}\n"
                f"  Temp. Parrilla: {self._temperatura_parrilla}°C\n"
                f"  Carbón: {self._carbon_disponible:.1f} kg {carbon_alerta}")
    
    def __repr__(self) -> str:
        return f"EstacionParrilla(ordenes={self.contar_ordenes_totales()}, carbon={self._carbon_disponible:.1f}kg)"

# ================================================================================
# ARCHIVO 6/9: estacion_pastas.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/estacion_pastas.py
# ================================================================================

from datetime import datetime
from typing import Optional
from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.entidades.cocina.orden_cocina import OrdenCocina

class EstacionPastas(EstacionCocina):
    """Estación especializada en pastas"""
    
    def __init__(self):
        super().__init__(nombre_estacion="Pastas", capacidad_maxima=6)
        self._agua_hirviendo = False
        self._ollas_disponibles = 4
        self._cantidad_pasta_kg = 50.0  # kg disponibles
        self._ultima_limpieza = None
    
    # --- GETTERS ESPECÍFICOS ---
    def get_ollas_disponibles(self) -> int:
        return self._ollas_disponibles
    
    def get_cantidad_pasta(self) -> float:
        return self._cantidad_pasta_kg
    
    def esta_agua_hirviendo(self) -> bool:
        return self._agua_hirviendo
    
    # --- OPERACIONES ---
    def calentar_agua(self):
        """Calienta el agua para cocinar"""
        self._agua_hirviendo = True
        self._temperatura_actual = 100.0
    
    def enfriar_agua(self):
        """Enfría el agua"""
        self._agua_hirviendo = False
        self._temperatura_actual = 20.0
    
    def agregar_pasta(self, cantidad_kg: float):
        """Agrega pasta al inventario"""
        if cantidad_kg <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self._cantidad_pasta_kg += cantidad_kg
    
    def consumir_pasta(self, cantidad_kg: float = 0.3):
        """Consume pasta al preparar un plato"""
        if self._cantidad_pasta_kg < cantidad_kg:
            raise ValueError("No hay suficiente pasta")
        self._cantidad_pasta_kg -= cantidad_kg
    
    def usar_olla(self):
        """Marca una olla como en uso"""
        if self._ollas_disponibles <= 0:
            raise ValueError("No hay ollas disponibles")
        self._ollas_disponibles -= 1
    
    def liberar_olla(self):
        """Libera una olla"""
        if self._ollas_disponibles >= 4:
            raise ValueError("Todas las ollas ya están libres")
        self._ollas_disponibles += 1
    
    # --- OVERRIDE DE MÉTODOS ABSTRACTOS ---
    def verificar_equipamiento(self) -> bool:
        """Verifica que se pueda cocinar pasta"""
        if not self._agua_hirviendo:
            return False
        if self._ollas_disponibles <= 0:
            return False
        if self._cantidad_pasta_kg < 1.0:
            return False
        return True
    
    def realizar_mantenimiento(self):
        """Realiza limpieza de la estación"""
        self._ultima_limpieza = datetime.now()
        self.limpiar_ordenes_completadas()
    
    def obtener_temperatura_operacion(self) -> tuple:
        """Rango óptimo de temperatura"""
        return (18, 28)  # °C ambiente
    
    # --- VALIDACIONES ---
    def necesita_pasta(self) -> bool:
        """Verifica si necesita reposición de pasta"""
        return self._cantidad_pasta_kg < 10.0
    
    def puede_cocinar_pasta(self) -> bool:
        """Verifica si puede cocinar pasta"""
        return (self._agua_hirviendo and 
                self._ollas_disponibles > 0 and 
                self._cantidad_pasta_kg >= 0.3)
    
    # --- OVERRIDE DE COMPLETAR ORDEN ---
    def completar_orden(self, orden_id: int):
        """Override para liberar olla y consumir pasta"""
        resultado = super().completar_orden(orden_id)
        if resultado:
            self.liberar_olla()
            self.consumir_pasta()
        return resultado
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        agua_estado = "💧 Hirviendo" if self._agua_hirviendo else "💧 Fría"
        pasta_alerta = "⚠️ BAJO" if self.necesita_pasta() else "✓"
        
        return (f"{base_str}\n"
                f"  Agua: {agua_estado}\n"
                f"  Ollas disponibles: {self._ollas_disponibles}/4\n"
                f"  Pasta: {self._cantidad_pasta_kg:.1f} kg {pasta_alerta}")
    
    def __repr__(self) -> str:
        return f"EstacionPastas(ordenes={self.contar_ordenes_totales()}, pasta={self._cantidad_pasta_kg:.1f}kg)"


# ================================================================================
# ARCHIVO 7/9: estacion_postres.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/estacion_postres.py
# ================================================================================

from datetime import datetime
from src.entidades.cocina.estacion_cocina import EstacionCocina
from src.entidades.cocina.orden_cocina import OrdenCocina

class EstacionPostres(EstacionCocina):
    """Estación especializada en postres"""
    
    def __init__(self):
        super().__init__(nombre_estacion="Postres", capacidad_maxima=5)
        self._heladera_encendida = True
        self._temperatura_heladera = -5.0  # °C
        self._horno_encendido = False
        self._temperatura_horno = 0.0
        self._ultima_limpieza = None
    
    # --- GETTERS ESPECÍFICOS ---
    def get_temperatura_heladera(self) -> float:
        return self._temperatura_heladera
    
    def get_temperatura_horno(self) -> float:
        return self._temperatura_horno
    
    def esta_heladera_encendida(self) -> bool:
        return self._heladera_encendida
    
    def esta_horno_encendido(self) -> bool:
        return self._horno_encendido
    
    # --- OPERACIONES ---
    def encender_horno(self, temperatura: float = 180.0):
        """Enciende el horno de postres"""
        if temperatura < 100 or temperatura > 250:
            raise ValueError("Temperatura fuera de rango (100-250°C)")
        self._horno_encendido = True
        self._temperatura_horno = temperatura
    
    def apagar_horno(self):
        """Apaga el horno"""
        self._horno_encendido = False
        self._temperatura_horno = 0.0
    
    def ajustar_temperatura_horno(self, temperatura: float):
        """Ajusta la temperatura del horno"""
        if not self._horno_encendido:
            raise ValueError("El horno no está encendido")
        if temperatura < 100 or temperatura > 250:
            raise ValueError("Temperatura fuera de rango")
        self._temperatura_horno = temperatura
    
    def ajustar_temperatura_heladera(self, temperatura: float):
        """Ajusta la temperatura de la heladera"""
        if temperatura > 5:
            raise ValueError("La heladera debe estar bajo 5°C")
        self._temperatura_heladera = temperatura
    
    # --- OVERRIDE DE MÉTODOS ABSTRACTOS ---
    def verificar_equipamiento(self) -> bool:
        """Verifica que el equipamiento esté funcionando"""
        if not self._heladera_encendida:
            return False
        if self._temperatura_heladera > 5:
            return False
        return True
    
    def realizar_mantenimiento(self):
        """Realiza mantenimiento de la estación"""
        self._ultima_limpieza = datetime.now()
        self.limpiar_ordenes_completadas()
    
    def obtener_temperatura_operacion(self) -> tuple:
        """Rango óptimo de temperatura ambiente"""
        return (18, 24)  # °C
    
    # --- VALIDACIONES ---
    def puede_hacer_postres_frios(self) -> bool:
        """Verifica si puede hacer postres fríos"""
        return self._heladera_encendida and self._temperatura_heladera <= 0
    
    def puede_hornear(self) -> bool:
        """Verifica si puede hornear postres"""
        return self._horno_encendido and self._temperatura_horno >= 150
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        base_str = super().__str__()
        
        heladera_estado = f"❄️ {self._temperatura_heladera}°C" if self._heladera_encendida else "❄️ Apagada"
        horno_estado = f"🔥 {self._temperatura_horno}°C" if self._horno_encendido else "🔥 Apagado"
        
        return (f"{base_str}\n"
                f"  Heladera: {heladera_estado}\n"
                f"  Horno: {horno_estado}")
    
    def __repr__(self) -> str:
        return f"EstacionPostres(ordenes={self.contar_ordenes_totales()})"

# ================================================================================
# ARCHIVO 8/9: estado_orden.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/estado_orden.py
# ================================================================================

from enum import Enum

class EstadoOrden(Enum):
    """Estados posibles de una orden en cocina"""
    PENDIENTE = "Pendiente"
    EN_PREPARACION = "En Preparación"
    LISTA = "Lista"
    ENTREGADA = "Entregada"
    CANCELADA = "Cancelada"
    
    def __str__(self):
        return self.value

# ================================================================================
# ARCHIVO 9/9: orden_cocina.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/entidades/cocina/orden_cocina.py
# ================================================================================

from datetime import datetime
from typing import Optional
from src.entidades.cocina.estado_orden import EstadoOrden
from src.entidades.pedidos.item_pedido import ItemPedido


class OrdenCocina:
    """Representa una orden individual en la cocina para un item específico"""
    
    _contador_id = 0
    
    def __init__(self, item_pedido: ItemPedido, pedido_id: int, mesa_id: Optional[int] = None):
        OrdenCocina._contador_id += 1
        self._id = OrdenCocina._contador_id
        self._item_pedido = item_pedido
        self._pedido_id = pedido_id
        self._mesa_id = mesa_id
        self._estado = EstadoOrden.PENDIENTE
        self._estacion_asignada = item_pedido.get_item_menu().get_estacion_cocina()
        self._prioridad = 1  # 1=normal, 2=alta, 3=urgente
        self._chef_asignado_id: Optional[int] = None
        
        # Tiempos
        self._fecha_hora_creacion = datetime.now()
        self._fecha_hora_inicio: Optional[datetime] = None
        self._fecha_hora_fin: Optional[datetime] = None
        
        # Observaciones
        self._notas_chef = ""
        self._observaciones_cliente = item_pedido.get_observaciones_especiales()
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_item_pedido(self) -> ItemPedido:
        return self._item_pedido
    
    def get_pedido_id(self) -> int:
        return self._pedido_id
    
    def get_mesa_id(self) -> Optional[int]:
        return self._mesa_id
    
    def get_estado(self) -> EstadoOrden:
        return self._estado
    
    def get_estacion_asignada(self) -> str:
        return self._estacion_asignada
    
    def get_prioridad(self) -> int:
        return self._prioridad
    
    def get_chef_asignado_id(self) -> Optional[int]:
        return self._chef_asignado_id
    
    def get_fecha_hora_creacion(self) -> datetime:
        return self._fecha_hora_creacion
    
    def get_notas_chef(self) -> str:
        return self._notas_chef
    
    def get_observaciones_cliente(self) -> str:
        return self._observaciones_cliente
    
    # --- SETTERS ---
    def set_prioridad(self, prioridad: int):
        """Establece la prioridad: 1=normal, 2=alta, 3=urgente"""
        if prioridad not in [1, 2, 3]:
            raise ValueError("La prioridad debe ser 1, 2 o 3")
        self._prioridad = prioridad
    
    def set_chef_asignado(self, chef_id: int):
        self._chef_asignado_id = chef_id
    
    def agregar_nota_chef(self, nota: str):
        """Agrega una nota del chef sobre la preparación"""
        if self._notas_chef:
            self._notas_chef += f"\n- {nota}"
        else:
            self._notas_chef = f"- {nota}"
    
    # --- GESTIÓN DE ESTADO ---
    def iniciar_preparacion(self):
        """Marca la orden como en preparación"""
        if self._estado != EstadoOrden.PENDIENTE:
            raise ValueError(f"No se puede iniciar una orden en estado {self._estado}")
        self._estado = EstadoOrden.EN_PREPARACION
        self._fecha_hora_inicio = datetime.now()
    
    def marcar_como_lista(self):
        """Marca la orden como lista para servir"""
        if self._estado != EstadoOrden.EN_PREPARACION:
            raise ValueError(f"No se puede marcar como lista una orden en estado {self._estado}")
        self._estado = EstadoOrden.LISTA
        self._fecha_hora_fin = datetime.now()
    
    def marcar_como_entregada(self):
        """Marca la orden como entregada al cliente"""
        if self._estado != EstadoOrden.LISTA:
            raise ValueError(f"No se puede entregar una orden en estado {self._estado}")
        self._estado = EstadoOrden.ENTREGADA
    
    def cancelar(self, motivo: str = ""):
        """Cancela la orden"""
        if self._estado == EstadoOrden.ENTREGADA:
            raise ValueError("No se puede cancelar una orden ya entregada")
        self._estado = EstadoOrden.CANCELADA
        if motivo:
            self.agregar_nota_chef(f"CANCELADA: {motivo}")
    
    # --- CÁLCULOS DE TIEMPO ---
    def calcular_tiempo_preparacion(self) -> Optional[int]:
        """Calcula el tiempo real de preparación en minutos"""
        if not self._fecha_hora_inicio or not self._fecha_hora_fin:
            return None
        delta = self._fecha_hora_fin - self._fecha_hora_inicio
        return int(delta.total_seconds() / 60)
    
    def calcular_tiempo_espera_actual(self) -> int:
        """Calcula el tiempo de espera desde la creación hasta ahora"""
        delta = datetime.now() - self._fecha_hora_creacion
        return int(delta.total_seconds() / 60)
    
    def get_tiempo_estimado(self) -> int:
        """Retorna el tiempo estimado de preparación del item"""
        return self._item_pedido.get_item_menu().get_tiempo_preparacion()
    
    def esta_retrasada(self) -> bool:
        """Verifica si la orden está retrasada respecto al tiempo estimado"""
        if self._estado in [EstadoOrden.LISTA, EstadoOrden.ENTREGADA, EstadoOrden.CANCELADA]:
            return False
        return self.calcular_tiempo_espera_actual() > self.get_tiempo_estimado()
    
    # --- VALIDACIONES ---
    def puede_iniciarse(self) -> bool:
        """Verifica si la orden puede iniciarse"""
        return self._estado == EstadoOrden.PENDIENTE and self._chef_asignado_id is not None
    
    def esta_en_progreso(self) -> bool:
        """Verifica si la orden está siendo preparada"""
        return self._estado == EstadoOrden.EN_PREPARACION
    
    def esta_completada(self) -> bool:
        """Verifica si la orden está completada (lista o entregada)"""
        return self._estado in [EstadoOrden.LISTA, EstadoOrden.ENTREGADA]
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado_emoji = {
            EstadoOrden.PENDIENTE: "⏳",
            EstadoOrden.EN_PREPARACION: "👨‍🍳",
            EstadoOrden.LISTA: "✅",
            EstadoOrden.ENTREGADA: "🍽️",
            EstadoOrden.CANCELADA: "❌"
        }
        
        prioridad_str = "🔴 URGENTE" if self._prioridad == 3 else "🟡 ALTA" if self._prioridad == 2 else "🟢 NORMAL"
        
        mesa_str = f"Mesa {self._mesa_id}" if self._mesa_id else "Para llevar"
        
        tiempo_info = ""
        if self._estado == EstadoOrden.EN_PREPARACION:
            tiempo_info = f"\n  ⏱️ Tiempo transcurrido: {self.calcular_tiempo_espera_actual()} min"
            if self.esta_retrasada():
                tiempo_info += " ⚠️ RETRASADA"
        elif self._fecha_hora_fin:
            tiempo_real = self.calcular_tiempo_preparacion()
            tiempo_info = f"\n  ✓ Tiempo de preparación: {tiempo_real} min"
        
        obs_cliente = f"\n  💬 Cliente: {self._observaciones_cliente}" if self._observaciones_cliente else ""
        notas_chef = f"\n  📝 Chef: {self._notas_chef}" if self._notas_chef else ""
        
        return (f"{estado_emoji.get(self._estado, '📋')} Orden #{self._id} - {prioridad_str}\n"
                f"  Pedido #{self._pedido_id} - {mesa_str}\n"
                f"  Item: {self._item_pedido.get_item_menu().get_nombre()} x{self._item_pedido.get_cantidad()}\n"
                f"  Estación: {self._estacion_asignada}\n"
                f"  Estado: {self._estado.value}\n"
                f"  Estimado: {self.get_tiempo_estimado()} min"
                f"{tiempo_info}"
                f"{obs_cliente}"
                f"{notas_chef}")
    
    def __repr__(self) -> str:
        return (f"OrdenCocina(id={self._id}, "
                f"pedido={self._pedido_id}, "
                f"estado={self._estado}, "
                f"estacion={self._estacion_asignada})")

