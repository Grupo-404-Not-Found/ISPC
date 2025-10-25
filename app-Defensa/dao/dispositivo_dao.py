from app.conn.db_conn import Connection
from app.dao.interfaces.i_dispositivo_dao import IDispositivoDAO
from app.dominio.dispositivo import Dispositivo

class DispositivoDAO(IDispositivoDAO):
    """Implementación de acceso a datos para dispositivos."""

    def crear(self, user_id, terminal_id, nombre, tipo, numero_serie):
        with Connection() as cursor:
            cursor.execute(
                """
                INSERT INTO dispositivos (user_id, terminal_id, nombre, tipo, numero_serie)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (user_id, terminal_id, nombre, tipo, numero_serie)
            )

    def obtener_por_usuario(self, user_id):
        with Connection() as cursor:
            cursor.execute("SELECT * FROM dispositivos WHERE user_id = %s", (user_id,))
            rows = cursor.fetchall()
            return [Dispositivo(nombre=r["nombre"], tipo=r["tipo"], estado=r["estado"]) for r in rows]

    def eliminar(self, device_id):
        with Connection() as cursor:
            cursor.execute("DELETE FROM dispositivos WHERE device_id = %s", (device_id,))