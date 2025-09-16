from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .modelo import SistemaSmartHome, Camara

class Automatizacion(ABC):
    def __init__(self, nombre: str, descripcion: str = "") -> None:
        self.nombre = nombre
        self.descripcion = descripcion

    @abstractmethod
    def ejecutar(self, sistema: "SistemaSmartHome") -> None:
        ...

class AutomatizacionAhorroEnergia(Automatizacion):
    def __init__(self) -> None:
        super().__init__(nombre="Ahorro de energía", descripcion="Apaga todo salvo cámaras")

    def ejecutar(self, sistema: "SistemaSmartHome") -> None:
        # apaga todos los dispositivos excepto las cámaras
        from .modelo import Camara
        for d in sistema.dispositivos:
            if not isinstance(d, Camara):
                d.apagar()
