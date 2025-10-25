from abc import ABC, abstractmethod

class Automatizacion(ABC):
    def __init__(self, nombre: str, descripcion: str = "") -> None:
        self._nombre = nombre
        self._descripcion = descripcion

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def ejecutar(self, sistema):
        pass


class AutomatizacionAhorroEnergia(Automatizacion):
    def __init__(self):
        super().__init__("Ahorro de energía", "Apaga todo salvo las luces principales")

    def ejecutar(self, sistema):
        for d in sistema.dispositivos:
            if d.tipo != "luz":
                d.apagar()