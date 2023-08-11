import cx_Oracle

from db_utils import connect_to_database

def delete_usuario(conn, usuario_id):
    cursor = conn.cursor()
    try:
        delete_query = "DELETE FROM Usuario WHERE id_usuario = :1"
        cursor.execute(delete_query, (usuario_id,))
        rows_deleted = cursor.rowcount
        if rows_deleted == 0:
            print("Erro: Usuário não encontrado.")
        else:
            conn.commit()
            print("Usuário excluído com sucesso!")
    except cx_Oracle.Error as error:
        print("Erro:", error)
    finally:
        cursor.close()

def delete_alimentos(conn, alimento_id):
    cursor = conn.cursor()
    try:
        delete_query = "DELETE FROM Alimentos WHERE id_alimento = :1"
        cursor.execute(delete_query, (alimento_id,))
        rows_deleted = cursor.rowcount
        if rows_deleted == 0:
            print("Erro: Alimento não encontrado.")
        else:
            conn.commit()
            print("Alimento excluído com sucesso!")
    except cx_Oracle.Error as error:
        print("Erro:", error)
    finally:
        cursor.close()
