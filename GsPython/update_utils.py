import cx_Oracle

from db_utils import connect_to_database

def update_usuario(conn, usuario):
    cursor = conn.cursor()
    try:
        update_query = """
            UPDATE Usuario SET nome_completo = :1, email = :2, cpf = :3, senha = :4, cep = :5, endereco = :6, bairro = :7, cidade = :8, estado = :9
            WHERE id_usuario = :10
        """
        cursor.execute(update_query, (
            usuario['nome'],
            usuario['email'],
            usuario['cpf'],
            usuario['senha'],
            usuario['cep'],
            usuario['endereco'],
            usuario['bairro'],
            usuario['cidade'],
            usuario['estado'],
            usuario['id']
        ))
        rows_updated = cursor.rowcount
        if rows_updated == 0:
            print("Erro: Usuário não encontrado.")
        else:
            conn.commit()
            print("Usuário atualizado com sucesso!")
    except cx_Oracle.Error as error:
        print("Erro:", error)
    finally:
        cursor.close()

def update_alimentos(conn, alimentos):
    cursor = conn.cursor()
    try:
        update_query = """
            UPDATE Alimentos SET nome_alimento = :1, quantidade = :2, data_validade = TO_DATE(:3, 'YYYY-MM-DD'), id_fonte = :4
            WHERE id_alimento = :5
        """
        cursor.execute(update_query, (
            alimentos['nome_alimento'],
            alimentos['quantidade'],
            alimentos['data_validade'],
            alimentos['id_fonte'],
            alimentos['id']
        ))
        rows_updated = cursor.rowcount
        if rows_updated == 0:
            print("Erro: Alimento não encontrado.")
        else:
            conn.commit()
            print("Alimento atualizado com sucesso!")
    except cx_Oracle.Error as error:
        print("Erro:", error)
    finally:
        cursor.close()
