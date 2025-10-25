from abc import ABC, abstractmethod

class IDispositivoDAO(ABC):
    """Interfaz para definir operaciones CRUD de dispositivos."""

    @abstractmethod
    def crear(self, user_id, terminal_id, nombre, tipo, numero_serie):
        pass

    @abstractmethod
    def obtener_por_usuario(self, user_id):
        pass

    @abstractmethod
    def eliminar(self, device_id):
        pass