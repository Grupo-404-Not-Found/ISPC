from dispositivos import listar_dispositivos, agregar_dispositivo, eliminar_dispositivo, buscar_dispositivo
from automatizacion import ejecutar_automatizacion
from usuarios import registrar_usuario, iniciar_sesion, ver_datos_personales, modificar_rol, usuarios

"""
def grupo(los_404_not_found):
    integrantes = [
        "Camolotto Alejo Nicolas - DNI 44.606.044",
        "Flores Lopez Giancarlo - DNI 95.113.172",
        "Quevedo Jorge Francisco - DNI 31.218.408",
        "Quevedo Oscar Alberto - DNI 34.839.723"
    ]

    print(f"Grupo: {los_404_not_found}")
    print("Integrantes:")
    for i, persona in enumerate(integrantes, 1):
        print(f"{i}. {persona}")

grupo("Los 404 Not Found")
"""
def menu_usuario_estandar(usuario, dispositivos):
    while True:
        print(f"\n--- Menú Usuario: {usuario['usuario']} (rol: estándar) ---")
        print("1. Ver mis datos personales")
        print("2. Ejecutar automatización")
        print("3. Ver dispositivos")
        print("4. Salir")
        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            ver_datos_personales(usuario)
        elif opcion == "2":
            ejecutar_automatizacion(dispositivos)
        elif opcion == "3":
            listar_dispositivos(dispositivos)
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida")


def menu_admin(usuario, dispositivos):
    while True:
        print(f"\n--- Menú Administrador: {usuario['usuario']} ---")
        print("1. Ver automatizaciones activas")
        print("2. Listar dispositivos")
        print("3. Agregar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Cambiar rol de un usuario")
        print("6. Salir")
        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            print("Automatización activa: Modo Ahorro de Energía")
        elif opcion == "2":
            listar_dispositivos(dispositivos)
        elif opcion == "3":
            agregar_dispositivo(dispositivos)
        elif opcion == "4":
            eliminar_dispositivo(dispositivos)
        elif opcion == "5":
            modificar_rol()
        elif opcion == "6":
            print("Cerrando sesión admin...")
            break
        else:
            print("Opción inválida")


def sistema():
    dispositivos = []
    print("\n--- Bienvenido al Sistema SmartHome ---")

    while True:
        print("\n1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            usuario = iniciar_sesion()
            if usuario:
                if usuario["rol"] == "admin":
                    menu_admin(usuario, dispositivos)
                else:
                    menu_usuario_estandar(usuario, dispositivos)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    sistema()
