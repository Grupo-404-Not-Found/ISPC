usuarios = []  # Lista de usuarios en memoria


def registrar_usuario():
    print("\n--- Registro de Usuario ---")
    usuario = input("Nombre de usuario: ")
    clave = input("Contraseña: ")

    for u in usuarios:
        if u["usuario"] == usuario:
            print("⚠️ Ya existe un usuario con ese nombre.")
            return None

    rol = "admin" if len(usuarios) == 0 else "estandar"

    nuevo_usuario = {
        "usuario": usuario,
        "clave": clave,
        "rol": rol
    }

    usuarios.append(nuevo_usuario)
    print(f"✅ Usuario registrado exitosamente con rol: {rol}")


def iniciar_sesion():
    print("\n🔐 Inicio de Sesión")
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

    for u in usuarios:
        if u["usuario"] == usuario and u["clave"] == clave:
            print(f"✅ Bienvenido, {usuario}. Rol: {u['rol']}")
            return u

    print("❌ Credenciales incorrectas.")
    return None


def ver_datos_personales(usuario):
    print("\n📇 Tus datos:")
    print(f"Usuario: {usuario['usuario']}")
    print(f"Rol: {usuario['rol']}")


def modificar_rol():
    print("\n🛠 Cambiar rol de un usuario")
    nombre = input("Nombre del usuario a modificar: ")

    for u in usuarios:
        if u["usuario"] == nombre:
            nuevo_rol = input("Nuevo rol (admin / estandar): ").lower()
            if nuevo_rol in ["admin", "estandar"]:
                u["rol"] = nuevo_rol
                print(f"✅ Rol actualizado a {nuevo_rol}.")
                return
            else:
                print("❌ Rol inválido.")
                return

    print("❌ Usuario no encontrado.")