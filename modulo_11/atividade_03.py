'''Criando uma tabela filtrada com sql '''

import sqlite3
import os

# Configuração inteligente de caminhos para evitar erros no VS Code
PATH_PASTA = os.path.dirname(os.path.abspath(__file__))
#  Criando o nome do banco aqui para não confundir com os outros exercícios
DB_NAME = os.path.join(PATH_PASTA, "banco_filtro_teste.db")

def inicializar_banco_novo():
    """Cria o banco novo e a tabela Clientes caso não existam."""
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    
    # Criando a tabela necessária para funcionar
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    );
    """)
    conexao.commit()
    conexao.close()

def inserir_dados_teste():
    """Insere alguns nomes variados para testarmos o filtro."""
    nomes = [
        ("Amanda Nada", "amanda@email.com"),
        ("Bruno Altos", "bruno@email.com"),
        ("Ivan Mobile", "ivan@email.com"),
        ("Alice Vieira", "alice@email.com"),
        ("Beatriz Lima", "beatriz@email.com")
    ]
    
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    for nome, email in nomes:
        try:
            cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))
        except sqlite3.IntegrityError:
            pass # Ignora se o e-mail já existir no banco
    conexao.commit()
    conexao.close()

def filtrar_clientes_por_letra(letra):
    """Busca e exibe apenas os clientes que começam com a letra informada."""
    try:
        conexao = sqlite3.connect(DB_NAME)
        cursor = conexao.cursor()
        
        # O operador LIKE com '%' faz o filtro (ex: 'A%' significa 'Começa com A')
        comando_sql = "SELECT * FROM Clientes WHERE nome LIKE ?"
        filtro = f"{letra}%"
        
        cursor.execute(comando_sql, (filtro,))
        resultados = cursor.fetchall()
        
        print(f"\n🔍 --- CLIENTES COM A LETRA '{letra.upper()}' ---")
        if not resultados:
            print("Nenhum cliente encontrado com esse critério.")
        else:
            for linha in resultados:
                print(f"ID: {linha[0]} | Nome: {linha[1]:<15} | E-mail: {linha[2]}")
        print("-" * 40)
        
    except Exception as e:
        print(f"❌ Erro na consulta: {e}")
    finally:
        conexao.close()



# 1. Aqui se cria o arquivo 'banco_filtro_teste.db' e a tabela Clientes
inicializar_banco_novo()

# 2. Aqui se insere as pessoas de teste
inserir_dados_teste()

# 3. E por fim executa o filtro de busca
filtrar_clientes_por_letra("I")