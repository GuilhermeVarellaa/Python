from insert_utils import insert_usuario, insert_alimento
from delete_utils import delete_usuario, delete_alimentos
from update_utils import update_usuario, update_alimentos
from select_utils import select_all_usuarios, select_all_alimentos
from db_utils import connect_to_database


def exibir_menu_usuarios():
    print("\nMENU DE USUÁRIOS")
    print("1. Inserir um novo usuário")
    print("2. Deletar um usuário")
    print("3. Alterar informações de um usuário")
    print("4. Selecionar todos os usuários")
    print("0. Voltar ao menu principal")


def exibir_menu_alimentos():
    print("\nMENU DE ALIMENTOS")
    print("1. Inserir um novo alimento")
    print("2. Deletar um alimento")
    print("3. Alterar informações de um alimento")
    print("4. Selecionar todos os alimentos")
    print("0. Voltar ao menu principal")


def ler_opcao():
    opcao = input("Opção: ")
    return opcao


def menu_usuarios(conn):
    while True:
        exibir_menu_usuarios()
        opcao = ler_opcao()

        if opcao == "1":
            novo_usuario = {
                'nome': input("Nome: "),
                'email': input("Email: "),
                'cpf': input("CPF: "),
                'senha': input("Senha: "),
                'cep': input("CEP: "),
                'endereco': input("Endereço: "),
                'bairro': input("Bairro: "),
                'cidade': input("Cidade: "),
                'estado': input("Estado: ")
            }
            insert_usuario(conn, novo_usuario)

        elif opcao == "2":
            usuario_id = input("ID do usuário a ser deletado: ")
            delete_usuario(conn, usuario_id)

        elif opcao == "3":
            usuario_id = input("ID do usuário a ser alterado: ")

            usuario = {
                'id': usuario_id,
                'nome': input("Novo nome: "),
                'email': input("Novo email: "),
                'cpf': input("Novo CPF: "),
                'senha': input("Nova senha: "),
                'cep': input("Novo CEP: "),
                'endereco': input("Novo endereço: "),
                'bairro': input("Novo bairro: "),
                'cidade': input("Nova cidade: "),
                'estado': input("Novo estado: ")
            }
            update_usuario(conn, usuario)

        elif opcao == "4":
            select_all_usuarios(conn)

        elif opcao == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")


def menu_alimentos(conn):
    while True:
        exibir_menu_alimentos()
        opcao = ler_opcao()

        # Dentro da função menu_alimentos

        if opcao == "1":
            novo_alimento = {
                'nome_alimento': input("Nome do alimento: "),
                'quantidade': input("Quantidade: "),
                'data_validade': input("Data de validade (AAAA-MM-DD): "),
                'id_fonte': input("ID da fonte: ")
            }
            insert_alimento(conn, novo_alimento)



        elif opcao == "2":
            alimento_id = input("ID do alimento a ser deletado: ")
            delete_alimentos(conn, alimento_id)

        elif opcao == "3":
            alimento_id = input("ID do alimento a ser alterado: ")

            alimento = {
                'id': alimento_id,
                'nome_alimento': input("Novo nome do alimento: "),
                'quantidade': input("Nova quantidade: "),
                'data_validade': input("Nova data de validade (AAAA-MM-DD): "),
                'id_fonte': input("Novo ID da fonte: ")
            }
            update_alimentos(conn, alimento)

        elif opcao == "4":
            select_all_alimentos(conn)

        elif opcao == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")


def main():
    # Conexão com o banco de dados
    conn = connect_to_database()

    while True:
        print("\nMENU PRINCIPAL")
        print("1. Menu de Usuários")
        print("2. Menu de Alimentos")
        print("0. Sair")

        opcao = ler_opcao()

        if opcao == "1":
            menu_usuarios(conn)

        elif opcao == "2":
            menu_alimentos(conn)

        elif opcao == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")

    # Fechar conexão com o banco de dados
    conn.close()


if __name__ == '__main__':
    main()
