from database import conectar

def criar_tabela_alunos():
    conexao, cursor = conectar()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()

    print("Tabela criada com sucesso!")


def adicionar_aluno(nome, email):
    conexao, cursor = conectar()

    sql_insert = "INSERT INTO alunos (nome, email ) VALUES (?, ?)"
    cursor.execute(sql_insert, (nome, email))

    conexao.commit()

    print(f"\nAluno {nome} adicionado com sucesso!")
    conexao.close()


def listar_alunos():
    conexao, cursor = conectar()

    cursor.execute("SELECT * FROM alunos")
    lista_alunos = cursor.fetchall()

    print("\n****** Lista de Alunos ******")
    for aluno in lista_alunos:
        print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Email: {aluno[2]}")

    conexao.close()

    return lista_alunos

def atualizar_email(aluno_id, novo_email):
    conexao, cursor = conectar()

    sql_update = "UPDATE alunos SET email = ? WHERE id = ?"
    cursor.execute(sql_update, (novo_email, aluno_id))

    conexao.commit()

    print(f"O e-mail do Aluno ID {aluno_id} foi alterado para '{novo_email}'.")
    conexao.close()


def remover_aluno(aluno_id):
    conexao, cursor = conectar()

    sql_delete = "DELETE FROM alunos WHERE id = ?"
    cursor.execute(sql_delete, (aluno_id,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"\nAluno ID {aluno_id} foi removido do banco de dados.")
    else:
        print(f"\nAluno ID {aluno_id} não foi encontrado.")

    conexao.close()