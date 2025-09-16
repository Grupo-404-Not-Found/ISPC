from __future__ import annotations
from abc import ABC
from typing import List

class Usuario:
    def __init__(self, nombre_usuario: str, contraseña: str, rol: str = "user") -> None:
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.rol = rol
        self._sesion_activa = False

    def iniciar_sesion(self) -> None:
        self._sesion_activa = True

    def cerrar_sesion(self) -> None:
        self._sesion_activa = False

    @property
    def sesion_activa(self) -> bool:
        return self._sesion_activa


class Dispositivo(ABC):
    def __init__(self, nombre: str, tipo: str, estado: str = "apagado") -> None:
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado  # 'encendido' | 'apagado'

    def encender(self) -> None:
        self.estado = "encendido"

    def apagar(self) -> None:
        self.estado = "apagado"

    def mostrar_estado(self) -> str:
        return f"{self.nombre} ({self.tipo}): {self.estado}"


class Luz(Dispositivo):
    def __init__(self, nombre: str, estado: str = "apagado") -> None:
        super().__init__(nombre, tipo="luz", estado=estado)
        self.nivel = 100  # brillo por defecto

    def ajustar_luz(self, nivel: int) -> None:
        # normaliza a 0..100
        self.nivel = max(0, min(100, int(nivel)))


class Camara(Dispositivo):
    def __init__(self, nombre: str, estado: str = "encendido") -> None:
        # por defecto encendida (seguridad)
        super().__init__(nombre, tipo="cámara", estado=estado)
        self._grabando = False

    def grabar(self) -> None:
        self._grabando = True

    @property
    def grabando(self) -> bool:
        return self._grabando


class Electrodomestico(Dispositivo):
    def __init__(self, nombre: str, estado: str = "apagado") -> None:
        super().__init__(nombre, tipo="electrodoméstico", estado=estado)

    def ejecutar(self) -> None:
        self.encender()


class SistemaSmartHome:
    def __init__(self) -> None:
        self.usuarios: List[Usuario] = []
        self.dispositivos: List[Dispositivo] = []
        self.automatizaciones: List[object] = []  # objetos que exponen ejecutar(sistema)

    def agregar_usuario(self, usuario: Usuario) -> None:
        self.usuarios.append(usuario)

    def agregar_dispositivo(self, dispositivo: Dispositivo) -> None:
        self.dispositivos.append(dispositivo)

    def agregar_automatizacion(self, automatizacion: object) -> None:
        # duck typing: debe tener método ejecutar(sistema)
        self.automatizaciones.append(automatizacion)

    def listar_dispositivos(self) -> List[str]:
        return [d.mostrar_estado() for d in self.dispositivos]

    def ejecutar_automatizacion(self, nombre: str) -> None:
        for a in self.automatizaciones:
            if getattr(a, "nombre", None) == nombre:
                a.ejecutar(self)
                return
        raise ValueError(f"Automatización '{nombre}' no encontrada")
