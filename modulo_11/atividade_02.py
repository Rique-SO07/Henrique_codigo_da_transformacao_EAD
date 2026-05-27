'''Criando um sistema de banco de dados em CRUD'''
import sqlite3

DB_NAME = "sistema_cinema.db"

    # CREATE (Inserir dados)
def inserir_cliente(nome, email):
    try:
        conexao = sqlite3.connect(DB_NAME)
        cursor = conexao.cursor()
        
        comando = "INSERT INTO Clientes (nome, email) VALUES (?, ?)"
        # O uso do '?' protege o banco contra ataques de SQL Injection (Segurança!)
        cursor.execute(comando, (nome, email))
        
        conexao.commit()
        print(f"✅ Cliente '{nome}' inserido com sucesso!")
    except sqlite3.IntegrityError:
        print(f"❌ Erro: O e-mail '{email}' já está cadastrado!")
    finally:
        conexao.close()

    # READ (Consultar dados)
def consultar_clientes():
    try:
        conexao = sqlite3.connect(DB_NAME)
        cursor = conexao.cursor()
        
        cursor.execute("SELECT * FROM Clientes")
        # fetchall() traz todas as linhas encontradas no banco
        linhas = cursor.fetchall()
        
        print("\n--- 👥 LISTA DE CLIENTES ---")
        for linha in linhas:
            # linha[0] = id, linha[1] = nome, linha[2] = email
            print(f"ID: {linha[0]} | Nome: {linha[1]:<15} | E-mail: {linha[2]}")
        print("----------------------------")
    except Exception as e:
        print(f"Erro ao consultar: {e}")
    finally:
        conexao.close()

     #  UPDATE (Atualizar dados)
def atualizar_email_cliente(id_cliente, novo_email):
    try:
        conexao = sqlite3.connect(DB_NAME)
        cursor = conexao.cursor()
        
        comando = "UPDATE Clientes SET email = ? WHERE id = ?"
        cursor.execute(comando, (novo_email, id_cliente))
        
        conexao.commit()
        print(f"🔄 E-mail do ID {id_cliente} atualizado para '{novo_email}'!")
    except Exception as e:
        print(f"Erro ao atualizar: {e}")
    finally:
        conexao.close()

    # DELETE (Deletar dados)
def deletar_cliente(id_cliente):
    try:
        conexao = sqlite3.connect(DB_NAME)
        cursor = conexao.cursor()
        
        comando = "DELETE FROM Clientes WHERE id = ?"
        cursor.execute(comando, (id_cliente,)) # A vírgula é necessária quando passamos só 1 elemento na tupla
        
        conexao.commit()
        print(f"🗑️ Cliente com ID {id_cliente} foi removido do banco.")
    except Exception as e:
        print(f"Erro ao deletar: {e}")
    finally:
        conexao.close()

# Testando tudo

print("=== 1. Testando o CREATE ===")
inserir_cliente("Fredão Paiva", "fredaoo@email.com")
inserir_cliente("Ana Silva", "ana@email.com")
inserir_cliente("Carlos Souza", "carlos@email.com")

print("\n=== 2. Testando o READ ===")
consultar_clientes()

print("\n=== 3. Testando o UPDATE ===")
# Vamos corrigir o e-mail do Fredao se o ID dele for 1
atualizar_email_cliente(1, "fredao.novo@email.com")
consultar_clientes()

print("\n=== 4. Testando o DELETE ===")
# Vamos remover o cliente de ID 3 (Carlos)
deletar_cliente(3)
consultar_clientes()