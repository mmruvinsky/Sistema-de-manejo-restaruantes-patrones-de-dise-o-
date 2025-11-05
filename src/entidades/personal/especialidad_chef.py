# src/entidades/personal/especialidad_chef.py

from enum import Enum

class EspecialidadChef(Enum):
    """
    Define las especialidades y rangos de los chefs en la cocina.
    """
    
    # Rangos jerárquicos
    CHEF_EJECUTIVO = "Chef Ejecutivo"
    SOUS_CHEF = "Sous Chef"
    
    # Especialidades de estación
    PARRILLA = "Parrilla"
    PASTAS = "Pastas"
    REPOSTERIA = "Repostería"
    GARDE_MANGER = "Garde Manger (Fríos)"
    COCINA_GENERAL = "Cocina General"
    
    def __str__(self):
        """Retorna el valor legible de la especialidad."""
        return self.value