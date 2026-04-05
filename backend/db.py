import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="evolut_db",
        user="postgres",
        password="3134553"
    )

    conn.set_client_encoding('UTF8')

    return conn