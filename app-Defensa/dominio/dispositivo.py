from abc import ABC, abstractmethod

class Dispositivo(ABC):
    def __init__(self, nombre: str, tipo: str, estado: str = "apagado") -> None:
        self._nombre = nombre
        self._tipo = tipo
        self._estado = estado

    # --- Propiedades ---
    @property
    def nombre(self):
        return self._nombre

    @property
    def tipo(self):
        return self._tipo

    @property
    def estado(self):
        return self._estado

    # --- Métodos comunes ---
    def encender(self):
        self._estado = "encendido"

    def apagar(self):
        self._estado = "apagado"

    def mostrar_estado(self):
        return f"{self._nombre} ({self._tipo}): {self._estado}"


class Luz(Dispositivo):
    def __init__(self, nombre: str, estado: str = "apagado") -> None:
        super().__init__(nombre, tipo="luz", estado=estado)
        self._nivel = 100  # brillo por defecto

    @property
    def nivel(self):
        return self._nivel

    def ajustar_luz(self, nivel: int):
        self._nivel = max(0, min(100, int(nivel)))


class Electrodomestico(Dispositivo):
    def __init__(self, nombre: str, estado: str = "apagado") -> None:
        super().__init__(nombre, tipo="electrodoméstico", estado=estado)

    def ejecutar(self):
        self.encender()