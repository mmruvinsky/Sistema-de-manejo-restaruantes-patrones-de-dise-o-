from enum import Enum

class CategoriaItem(Enum):
    ENTRADA = "Entrada"
    PLATO_PRINCIPAL = "Plato Principal"
    POSTRE = "Postre"
    BEBIDA = "Bebida"
    OTRO = "Otro"

    def __str__(self):
        return self.value