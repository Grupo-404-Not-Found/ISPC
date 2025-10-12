import mysql.connector
from mysql.connector import pooling
from app.config import DB_CONFIG

# Crear pool de conexiones
try:
    connection_pool = pooling.MySQLConnectionPool(
        pool_name="smarthome_pool",
        pool_size=5,
        **DB_CONFIG
    )
    print("Pool de conexiones creado exitosamente.")
except mysql.connector.Error as err:
    print(f"Error al crear el pool de conexiones: {err}")
    connection_pool = None

def get_connection():
    """Devuelve una conexión activa desde el pool."""
    if connection_pool:
        try:
            return connection_pool.get_connection()
        except mysql.connector.Error as err:
            print(f"Error al obtener una conexión del pool: {err}")
            return None
    else:
        print("El pool de conexiones no está disponible.")
        return None