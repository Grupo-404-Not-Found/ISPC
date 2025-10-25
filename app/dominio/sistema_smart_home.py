from typing import List
from app.dominio.usuario import Usuario
from app.dominio.dispositivo import Dispositivo

class SistemaSmartHome:
    """Coordina usuarios, dispositivos y automatizaciones sin acceder a BD directamente."""

    def __init__(self) -> None:
        self._usuarios: List[Usuario] = []
        self._dispositivos: List[Dispositivo] = []
        self._automatizaciones: List[object] = []

    # --- Gestión de usuarios ---
    def agregar_usuario(self, usuario: Usuario):
        self._usuarios.append(usuario)

    def listar_usuarios(self):
        return [str(u) for u in self._usuarios]

    # --- Gestión de dispositivos ---
    def agregar_dispositivo(self, dispositivo: Dispositivo):
        self._dispositivos.append(dispositivo)

    def listar_dispositivos(self):
        return [d.mostrar_estado() for d in self._dispositivos]

    @property
    def dispositivos(self):
        return self._dispositivos

    # --- Automatizaciones ---
    def agregar_automatizacion(self, automatizacion):
        self._automatizaciones.append(automatizacion)

    def ejecutar_automatizacion(self, nombre: str):
        for a in self._automatizaciones:
            if getattr(a, "nombre", None) == nombre:
                a.ejecutar(self)
                return True
        return False