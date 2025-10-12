from db.persistencia import get_connection
from app.modelo import Camara

def create_camera(device_id: int, nombre: str, estado: str, file_path: str):
    """Inserta un nuevo registro de cámara."""
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO camaras (device_id, nombre, estado, file_path) VALUES (%s, %s, %s, %s)",
        (device_id, nombre, estado, file_path)
    )
    conn.commit()
    conn.close()

def get_camera_by_device_id(device_id: int):
    """Obtiene los datos de una cámara por el ID del dispositivo asociado."""
    conn = get_connection()
    if not conn:
        return None
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM camaras WHERE device_id = %s", (device_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    return row

def delete_camera_by_device_id(device_id: int):
    """Elimina una cámara usando el ID del dispositivo."""
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    cursor.execute("DELETE FROM camaras WHERE device_id = %s", (device_id,))
    conn.commit()
    conn.close()