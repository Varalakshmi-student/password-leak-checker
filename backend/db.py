import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="example@2026",
        database="password_leak_db"
    )

def check_password_hash(hash_value):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) AS is_leaked, source FROM leaked_passwords WHERE password_hash = %s GROUP BY source", (hash_value,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result