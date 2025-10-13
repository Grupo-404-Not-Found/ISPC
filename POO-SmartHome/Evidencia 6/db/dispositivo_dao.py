from db.persistencia import get_connection
from app.modelo import Dispositivo

def get_by_user(user_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM dispositivos WHERE user_id = %s", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    dispositivos = [Dispositivo(nombre=row["nombre"], tipo=row["tipo"], estado=row["estado"]) for row in rows]
    return dispositivos

def create_device(user_id: int, terminal_id: int, nombre: str, tipo: str, numero_serie: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO dispositivos (user_id, terminal_id, nombre, tipo, numero_serie) VALUES (%s, %s, %s, %s, %s)",
        (user_id, terminal_id, nombre, tipo, numero_serie)
    )
    conn.commit()
    conn.close()

def delete_device(device_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dispositivos WHERE device_id = %s", (device_id,))
    conn.commit()
    conn.close()