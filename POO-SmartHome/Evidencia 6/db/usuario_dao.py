from db.persistencia import get_connection
from app.modelo import Usuario

def get_by_username(username: str):
    conn = get_connection()
    if not conn:
        return None
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None
    # NOTA: En un sistema real, la contraseña no se debe almacenar ni comparar en texto plano.
    return Usuario(user_id=row["id"], nombre_usuario=row["username"], contraseña=row["password_hash"], rol=row.get("role", "user"))

def insert_user(username: str, email: str, password: str, role: str = "user"):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuarios (username, email, password_hash, role) VALUES (%s, %s, %s, %s)",
        (username, email, password, role)
    )
    conn.commit()
    conn.close()

def get_all_users():
    conn = get_connection()
    if not conn:
        return []
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, username, email, role, created_at FROM usuarios")
    users = cursor.fetchall()
    conn.close()
    return users

def update_user_role(user_id: int, role: str):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET role = %s WHERE id = %s", (role, user_id))
    conn.commit()
    conn.close()