def listar_dispositivos(dispositivos):
    if not dispositivos:
        print("No hay dispositivos registrados.")
    else:
        for i, d in enumerate(dispositivos, 1):
            print(f"{i}. {d['nombre']} - {d['tipo']} - {d['estado']}")

def buscar_dispositivo(dispositivos):
    nombre = input("Ingrese el nombre del dispositivo a buscar: ")
    encontrados = [d for d in dispositivos if d['nombre'].lower() == nombre.lower()]
    if encontrados:
        for d in encontrados:
            print(f"Encontrado: {d['nombre']} - {d['tipo']} - {d['estado']}")
    else:
        print("Dispositivo no encontrado.")

def agregar_dispositivo(dispositivos):
    nombre = input("Nombre del dispositivo: ")
    tipo = input("Tipo (luz, cámara, electrodoméstico, etc.): ")

    estado = input("Estado inicial (encendido/apagado): ").lower()
    while estado not in ["encendido", "apagado"]:
        print("Estado inválido. Debe ser 'encendido' o 'apagado'.")
        estado = input("Estado inicial (encendido/apagado): ").lower()

    dispositivo = {"nombre": nombre, "tipo": tipo, "estado": estado}
    dispositivos.append(dispositivo)
    print("Dispositivo agregado exitosamente.")

def eliminar_dispositivo(dispositivos):
    nombre = input("Nombre del dispositivo a eliminar: ")
    for d in dispositivos:
        if d['nombre'].lower() == nombre.lower():
            dispositivos.remove(d)
            print("Dispositivo eliminado.")
            return
    print("Dispositivo no encontrado.")