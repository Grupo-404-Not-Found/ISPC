import mysql.connector
from mysql.connector import pooling
from app.config import DB_CONFIG

# --- Pool de conexiones ---
_pool = pooling.MySQLConnectionPool(
    pool_name="smarthome_pool",
    pool_size=5,
    **DB_CONFIG
)

def get_connection():
    """Devuelve una conexión activa desde el pool."""
    return _pool.get_connection()

class Connection:
    """Context manager seguro para manejar cursor y conexión automáticamente."""
    def __enter__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor(dictionary=True)
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.cursor.close()
        self.conn.close()