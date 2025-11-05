"""
Archivo integrador generado automaticamente
Directorio: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/personal
Fecha: 2025-11-05 09:49:44
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: personal_service.py
# Ruta: /home/mmruvinsky/Documents/Facultad/Diseño de sistemas/Gestión restaurantes/Sistema-de-manejo-restaruantes-patrones-de-dise-o-/src/servicios/personal/personal_service.py
# ================================================================================

from typing import Dict, List, Optional
from src.entidades.personal.empleado import Empleado
from src.entidades.personal.chef import Chef
from src.entidades.personal.mozo import Mozo
from src.entidades.personal.cajero import Cajero

class PersonalService:
    """
    Servicio Singleton para gestionar todos los empleados.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_inicializado'):
            return
        self._empleados: Dict[int, Empleado] = {}
        self._inicializado = True
        print("Servicio de Personal inicializado.")

    def contratar_empleado(self, empleado: Empleado):
        if empleado.get_id() not in self._empleados:
            self._empleados[empleado.get_id()] = empleado
            print(f"Empleado contratado: {empleado.get_nombre_completo()} ({empleado.obtener_rol()})")
        
    def get_empleado(self, empleado_id: int) -> Optional[Empleado]:
        return self._empleados.get(empleado_id)
        
    def get_all_empleados(self) -> List[Empleado]:
        return list(self._empleados.values())
        
    def get_mozos_disponibles(self) -> List[Mozo]:
        return [
            e for e in self._empleados.values() 
            if isinstance(e, Mozo) and e.esta_activo()
        ]
        
    def get_chefs_disponibles(self) -> List[Chef]:
        return [
            e for e in self._empleados.values() 
            if isinstance(e, Chef) and e.esta_activo()
        ]

