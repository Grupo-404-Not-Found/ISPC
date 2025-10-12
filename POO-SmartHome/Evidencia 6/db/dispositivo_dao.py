from db.persistencia import get_connection
from app.modelo import Dispositivo, Camara, Luz, Electrodomestico

def get_by_user(user_id: int):
    conn = get_connection()
    if not conn:
        return []
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM dispositivos WHERE user_id = %s", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    
    dispositivos = []
    for row in rows:
        tipo = row["tipo"].lower()
        nombre = row["nombre"]
        estado = row["estado"]
        
        # Instancia la clase correcta según el tipo de dispositivo
        if tipo == "cámara":
            dispositivo = Camara(nombre=nombre, estado=estado)
        elif tipo == "luz":
            dispositivo = Luz(nombre=nombre, estado=estado)
        elif tipo == "electrodoméstico":
            dispositivo = Electrodomestico(nombre=nombre, estado=estado)
        else:
            # Fallback a un dispositivo genérico si el tipo no es específico
            dispositivo = Dispositivo(nombre=nombre, tipo=tipo, estado=estado)
        dispositivos.append(dispositivo)
        
    return dispositivos

def create_device(user_id: int, terminal_id: int, nombre: str, tipo: str, numero_serie: str):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO dispositivos (user_id, terminal_id, nombre, tipo, numero_serie) VALUES (%s, %s, %s, %s, %s)",
        (user_id, terminal_id, nombre, tipo, numero_serie)
    )
    conn.commit()
    conn.close()

def delete_device(device_id: int):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dispositivos WHERE device_id = %s", (device_id,))
    conn.commit()
    conn.close()