from alunos import (
    criar_tabela_alunos,
    adicionar_aluno,
    listar_alunos,
    atualizar_email,
    remover_aluno
)

def menu_principal():
    criar_tabela_alunos()

    while True:
        print('''
            \n ----- Sistema de Gerenciamento de Alunos -----
            [1] Adicionar Novo Aluno
            [2] Ver Lista de Alunos
            [3] Atualizar email de um Aluno
            [4] Remover Aluno da lista
            [5] Sair
        ''')

        escolha = int(input("Escolha a operação que deseja: "))

        if escolha == 1:
            nome = input("Digite o nome do aluno: ")
            email = input("Digite o email do aluno: ")

            adicionar_aluno(nome, email)

        elif escolha == 2:
            listar_alunos()

        elif escolha == 3:
            listar_alunos()
            aluno_id = int(input("Digite o id do aluno que deseja alterar o email: "))
            novo_email = input("Digite o novo Email: ")

            atualizar_email(aluno_id, novo_email)
        
        elif escolha == 4:
            listar_alunos()
            aluno_id = int(input("Digite o id do aluno que deseja remover: "))
            remover_aluno(aluno_id)

        elif escolha == 5:
            print("Encerrando o gerenciador...")
            break

        else:
            print("Opção inválida tente novamente!")


if __name__ == "__main__":
    menu_principal()