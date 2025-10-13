from db.persistencia import get_connection
conn = get_connection()
print(conn.is_connected())
conn.close()
