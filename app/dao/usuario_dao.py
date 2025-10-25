from app.conn.db_conn import Connection
from app.dao.interfaces.i_usuario_dao import IUsuarioDAO
from app.dominio.usuario import Usuario

class UsuarioDAO(IUsuarioDAO):
    """Implementación de acceso a datos para usuarios."""

    def insertar(self, username, email, password, role="user"):
        with Connection() as cursor:
            cursor.execute(
                "INSERT INTO usuarios (username, email, password_hash, role) VALUES (%s, %s, %s, %s)",
                (username, email, password, role)
            )

    def obtener_por_username(self, username):
        with Connection() as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
            row = cursor.fetchone()
            if not row:
                return None
            return Usuario(
                nombre_usuario=row["username"],
                contraseña=row["password_hash"],
                rol=row.get("role", "user")
            )

    def obtener_todos(self):
        with Connection() as cursor:
            cursor.execute("SELECT id, username, email, role, created_at FROM usuarios")
            return cursor.fetchall()

    def actualizar_rol(self, user_id, nuevo_rol):
        with Connection() as cursor:
            cursor.execute("UPDATE usuarios SET role = %s WHERE id = %s", (nuevo_rol, user_id))