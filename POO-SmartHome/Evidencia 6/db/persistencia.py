import mysql.connector
from mysql.connector import pooling
from app.config import DB_CONFIG

# Crear pool de conexiones (se inicializa automáticamente al importar)
connection_pool = pooling.MySQLConnectionPool(
    pool_name="smarthome_pool",
    pool_size=5,
    **DB_CONFIG
)

def get_connection():
    """Devuelve una conexión activa desde el pool."""
    return connection_pool.get_connection()
