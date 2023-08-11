import cx_Oracle

from db_utils import connect_to_database

def insert_usuario(conn, usuario):
    cursor = conn.cursor()
    try:
        insert_query = """
            INSERT INTO Usuario (nome_completo, email, cpf, senha, cep, endereco, bairro, cidade, estado)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)
        """
        cursor.execute(insert_query, (
            usuario['nome'],
            usuario['email'],
            usuario['cpf'],
            usuario['senha'],
            usuario['cep'],
            usuario['endereco'],
            usuario['bairro'],
            usuario['cidade'],
            usuario['estado']
        ))
        conn.commit()
        print("Usuário inserido com sucesso!")
    except cx_Oracle.IntegrityError as error:
        if "ORA-00001" in str(error):
            print("Erro: Já existe um usuário com o mesmo CPF.")
        else:
            print("Erro:", error)
    finally:
        cursor.close()

def insert_fonte_alimentos(conn, fonte_alimentos):
    cursor = conn.cursor()
    try:
        insert_query = """
            INSERT INTO FonteAlimentos (nome_fonte, tipo_fonte, localizacao)
            VALUES (:1, :2, :3)
        """
        cursor.execute(insert_query, (
            fonte_alimentos['nome_fonte'],
            fonte_alimentos['tipo_fonte'],
            fonte_alimentos['localizacao']
        ))
        conn.commit()
        print("Fonte de alimentos inserida com sucesso!")
    except cx_Oracle.Error as error:
        print("Erro:", error)
    finally:
        cursor.close()

def insert_alimento(conn, alimento):
    cursor = conn.cursor()
    try:
        insert_query = """
            INSERT INTO Alimentos (nome_alimento, quantidade, data_validade, id_fonte)
            VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4)
        """

        cursor.execute(insert_query, (
            alimento['nome_alimento'],
            alimento['quantidade'],
            alimento['data_validade'],
            alimento['id_fonte']
        ))

        conn.commit()
        print("Alimento inserido com sucesso!")
    except cx_Oracle.Error as error:
        print("Erro:", error)
    finally:
        cursor.close()





def insert_entregas(conn, entregas):
    cursor = conn.cursor()
    try:
        insert_query = """
            INSERT INTO Entregas (id_alimento, id_comunidade, quantidade, data_entrega)
            VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'))
        """
        cursor.execute(insert_query, (
            entregas['id_alimento'],
            entregas['id_comunidade'],
            entregas['quantidade'],
            entregas['data_entrega']
        ))
        conn.commit()
        print("Entrega inserida com sucesso!")
    except cx_Oracle.Error as error:
        print("Erro:", error)
    finally:
        cursor.close()
