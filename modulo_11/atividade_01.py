import sqlite3

def banco_de_dados():
    try:
        conexao = sqlite3.connect("sistema_cinema.db")
        cursor = conexao.cursor()
        print("\nConexão com o banco de dados estabelecida!")

        comando_sql = """
        CREATE TABLE IF NOT EXISTS Clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        );
        """

        cursor.execute(comando_sql)

        conexao.commit()
        print("\nTabela 'Clientes' criada (ou já criada) com sucesso!")

    except sqlite3.Error as erro:
        print(f"\n ❗ Erro ao manipular o banco de dados: {erro}")

    finally:
        if conexao:
            conexao.close()
            print("\nConexão com o banco de dados fechada com segurança.")
banco_de_dados()