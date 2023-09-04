
import psycopg2

def connect_to_database(db_params):
    try:
        conn = psycopg2.connect(**db_params)
        return conn
    except psycopg2.Error as e:
        print(f'Error: Unable to connect to the database: {e}')
        return None


def execute_sql_query(conn, query, data=None):
    try:
        cursor = conn.cursor()
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        conn.commit()
        return True
    except psycopg2.Error as e:
        print(f'Error: Unable to execute SQL query: {e}')
        conn.rollback()
        return False
    finally:
        cursor.close()


def close_database_connection(conn):
    conn.close()
