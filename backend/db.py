import os
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host=os.environ.get('MYSQLHOST', 'localhost'),
        user=os.environ.get('MYSQLUSER', 'root'),
        password=os.environ.get('MYSQLPASSWORD', 'example@2026'),
        database=os.environ.get('MYSQLDATABASE', 'password_leak_db'),
        port=int(os.environ.get('MYSQLPORT', 3306))
    )

def check_password_hash(hash_value):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            """
            SELECT COUNT(*) AS is_leaked, source 
            FROM leaked_passwords 
            WHERE password_hash = %s 
            GROUP BY source
            """,
            (hash_value,)
        )
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Database error: {e}")
        return []
    finally:
        cursor.close()
        conn.close()