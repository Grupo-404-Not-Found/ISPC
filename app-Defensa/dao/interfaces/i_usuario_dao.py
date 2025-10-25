from abc import ABC, abstractmethod

class IUsuarioDAO(ABC):
    """Interfaz para definir operaciones CRUD de usuarios."""

    @abstractmethod
    def insertar(self, username, email, password, role="user"):
        pass

    @abstractmethod
    def obtener_por_username(self, username):
        pass

    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def actualizar_rol(self, user_id, nuevo_rol):
        pass