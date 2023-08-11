import cx_Oracle

from db_utils import connect_to_database

def select_all_usuarios(conn):
    cursor = conn.cursor()
    try:
        select_query = "SELECT id_usuario, nome_completo, email FROM Usuario"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Nome: {row[1]}, Email: {row[2]}")
    except cx_Oracle.Error as error:
        print("Erro:", error)
    finally:
        cursor.close()

def select_all_alimentos(conn):
    cursor = conn.cursor()
    try:
        select_query = "SELECT id_alimento, nome_alimento, quantidade FROM Alimentos"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Alimento: {row[1]}, Quantidade: {row[2]}")
    except cx_Oracle.Error as error:
        print("Erro:", error)
    finally:
        cursor.close()
