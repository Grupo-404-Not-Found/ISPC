class Usuario:
    def __init__(self, nombre_usuario: str, contraseña: str, rol: str = "user") -> None:
        self._nombre_usuario = nombre_usuario
        self._contraseña = contraseña
        self._rol = rol
        self._sesion_activa = False

    # --- Propiedades (encapsulación) ---
    @property
    def nombre_usuario(self):
        return self._nombre_usuario

    @property
    def contraseña(self):
        return self._contraseña

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, nuevo_rol: str):
        self._rol = nuevo_rol

    @property
    def sesion_activa(self):
        return self._sesion_activa

    # --- Métodos de comportamiento ---
    def iniciar_sesion(self):
        self._sesion_activa = True

    def cerrar_sesion(self):
        self._sesion_activa = False

    def __str__(self):
        return f"Usuario({self._nombre_usuario}, rol={self._rol})"