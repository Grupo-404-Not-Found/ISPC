import sys
from getpass import getpass
from app.dao.usuario_dao import UsuarioDAO
from app.dao.dispositivo_dao import DispositivoDAO
from app.dominio.usuario import Usuario

# Instancias DAO
usuario_dao = UsuarioDAO()
dispositivo_dao = DispositivoDAO()

# ========================
#   FUNCIONES DE USUARIO
# ========================

def registrar_usuario():
    print("\n=== Registro de nuevo usuario ===")
    username = input("Nombre de usuario: ").strip()
    email = input("Correo electrónico: ").strip()
    password = getpass("Contraseña: ")

    if not username or not email or not password:
        print("Todos los campos son obligatorios.")
        return

    if usuario_dao.obtener_por_username(username):
        print("Ya existe un usuario con ese nombre.")
        return

    try:
        usuario_dao.insertar(username, email, password)
        print("Usuario registrado correctamente.")
    except Exception as e:
        print("Error al registrar usuario:", e)


def login():
    print("\n=== Inicio de sesión ===")
    username = input("Usuario: ").strip()
    password = getpass("Contraseña: ")

    user = usuario_dao.obtener_por_username(username)
    if not user or user.contraseña != password:
        print("Credenciales incorrectas.")
        return None

    user.iniciar_sesion()
    print(f"Bienvenido, {user.nombre_usuario} ({user.rol})")
    return user


# ========================
#   MENÚS DEL SISTEMA
# ========================

def menu_usuario(user: Usuario):
    while True:
        print("\n=== Menú Usuario ===")
        print("1. Ver mis datos")
        print("2. Ver mis dispositivos")
        print("3. Cerrar sesión")

        opcion = input("> ").strip()

        if opcion == "1":
            print(f"\nUsuario: {user.nombre_usuario}\nRol: {user.rol}")
        elif opcion == "2":
            try:
                dispositivos = dispositivo_dao.obtener_por_usuario(1)  # ID de ejemplo
                if not dispositivos:
                    print("No hay dispositivos registrados.")
                else:
                    print("\nMis dispositivos:")
                    for d in dispositivos:
                        print(f"- {d.mostrar_estado()}")
            except Exception as e:
                print("Error al consultar dispositivos:", e)
        elif opcion == "3":
            print("Cerrando sesión...")
            user.cerrar_sesion()
            break
        else:
            print("Opción inválida.")


def menu_admin(user: Usuario):
    while True:
        print("\n=== Menú Administrador ===")
        print("1. Ver todos los usuarios")
        print("2. Crear dispositivo")
        print("3. Eliminar dispositivo")
        print("4. Cambiar rol de usuario")
        print("5. Cerrar sesión")

        opcion = input("> ").strip()

        if opcion == "1":
            try:
                usuarios = usuario_dao.obtener_todos()
                if not usuarios:
                    print("No hay usuarios registrados.")
                else:
                    print("\nLista de usuarios:")
                    for u in usuarios:
                        print(f"ID {u['id']} | {u['username']} ({u['role']})")
            except Exception as e:
                print("Error al obtener usuarios:", e)

        elif opcion == "2":
            try:
                user_id = int(input("ID del usuario propietario: "))
                terminal_id = int(input("ID del terminal: "))
                nombre = input("Nombre del dispositivo: ").strip()
                tipo = input("Tipo: ").strip()
                numero_serie = input("Número de serie: ").strip()

                dispositivo_dao.crear(user_id, terminal_id, nombre, tipo, numero_serie)
                print("Dispositivo creado correctamente.")
            except Exception as e:
                print("Error al crear dispositivo:", e)

        elif opcion == "3":
            try:
                device_id = int(input("ID del dispositivo a eliminar: "))
                dispositivo_dao.eliminar(device_id)
                print("Dispositivo eliminado.")
            except Exception as e:
                print("Error al eliminar dispositivo:", e)

        elif opcion == "4":
            try:
                user_id = int(input("ID del usuario: "))
                nuevo_rol = input("Nuevo rol (admin/user): ").strip()
                if nuevo_rol not in ("admin", "user"):
                    print("Rol inválido.")
                else:
                    usuario_dao.actualizar_rol(user_id, nuevo_rol)
                    print("Rol actualizado.")
            except Exception as e:
                print("Error al cambiar rol:", e)

        elif opcion == "5":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida.")


# ========================
#       PROGRAMA PRINCIPAL
# ========================

def main():
    while True:
        print("\n=== SmartHome Console ===")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("> ").strip()

        if opcion == "1":
            user = login()
            if user:
                if user.rol == "admin":
                    menu_admin(user)
                else:
                    menu_usuario(user)
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            print("Hasta luego.")
            sys.exit()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()

