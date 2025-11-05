from datetime import datetime
from typing import Optional

class Cliente:
    """Representa un cliente del restaurante"""
    
    _contador_id = 0
    
    def __init__(self, nombre: str, telefono: str, email: Optional[str] = None):
        Cliente._contador_id += 1
        self._id = Cliente._contador_id
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
        self._fecha_registro = datetime.now()
        self._direccion = ""
        self._notas = ""  # Preferencias, alergias, etc.
        self._activo = True
    
    # --- GETTERS ---
    def get_id(self) -> int:
        return self._id
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def get_telefono(self) -> str:
        return self._telefono
    
    def get_email(self) -> Optional[str]:
        return self._email
    
    def get_fecha_registro(self) -> datetime:
        return self._fecha_registro
    
    def get_direccion(self) -> str:
        return self._direccion
    
    def get_notas(self) -> str:
        return self._notas
    
    def esta_activo(self) -> bool:
        return self._activo
    
    # --- SETTERS ---
    def set_nombre(self, nombre: str):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre
    
    def set_telefono(self, telefono: str):
        if not telefono or telefono.strip() == "":
            raise ValueError("El teléfono no puede estar vacío")
        self._telefono = telefono
    
    def set_email(self, email: str):
        self._email = email
    
    def set_direccion(self, direccion: str):
        self._direccion = direccion
    
    def set_notas(self, notas: str):
        """Notas sobre preferencias, alergias, etc."""
        self._notas = notas
    
    def set_activo(self, activo: bool):
        self._activo = activo
    
    # --- MÉTODOS ---
    def agregar_nota(self, nota: str):
        """Agrega una nota adicional a las existentes"""
        if self._notas:
            self._notas += f"\n- {nota}"
        else:
            self._notas = f"- {nota}"
    
    def tiempo_como_cliente(self) -> int:
        """Retorna los días desde el registro"""
        delta = datetime.now() - self._fecha_registro
        return delta.days
    
    def es_cliente_frecuente(self) -> bool:
        """Método base - se sobrescribe en ClienteFrecuente"""
        return False
    
    def aplicar_descuento(self) -> float:
        """Método base - clientes normales no tienen descuento"""
        return 0.0
    
    # --- REPRESENTACIÓN ---
    def __str__(self) -> str:
        estado = "✅ Activo" if self._activo else "❌ Inactivo"
        email_str = f"\n  Email: {self._email}" if self._email else ""
        direccion_str = f"\n  Dirección: {self._direccion}" if self._direccion else ""
        notas_str = f"\n  Notas: {self._notas}" if self._notas else ""
        
        return (f"👤 Cliente #{self._id}\n"
                f"  Nombre: {self._nombre}\n"
                f"  Teléfono: {self._telefono}"
                f"{email_str}"
                f"{direccion_str}"
                f"  Estado: {estado}\n"
                f"  Cliente desde: {self._fecha_registro.strftime('%d/%m/%Y')}"
                f"{notas_str}")
    
    def __repr__(self) -> str:
        return f"Cliente(id={self._id}, nombre='{self._nombre}')"