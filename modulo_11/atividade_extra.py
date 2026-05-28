'''Criando uma tabela de tarefas'''
import sqlite3
import os

#  Configuração segura de caminhos para o VS Code (do jeito que me atrapalho é melhor)
PATH_PASTA = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(PATH_PASTA, "gerenciador_tarefas.db")

def inicializar_banco():
    """Cria a tabela de tarefas se ela não existir."""
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL
    );
    """)
    conexao.commit()
    conexao.close()

def adicionar_tarefa(descricao):
    """Insere uma nova tarefa no banco de dados."""
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Tarefas (descricao) VALUES (?)", (descricao,))
    conexao.commit()
    conexao.close()
    print(f"\n✅ Tarefa '{descricao}' adicionada com sucesso!")

def visualizar_tarefas():
    """Busca e exibe todas as tarefas salvas."""
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Tarefas")
    tarefas = cursor.fetchall()
    conexao.close()

    print("\n === MINHAS TAREFAS ===")
    if not tarefas:
        print("Nenhuma tarefa pendente. Bom trabalho! 🎉")
    else:
        for t in tarefas:
            # t[0] é o ID, t[1] é a descrição da tarefa
            print(f"[{t[0]}] - {t[1]}")
    print("=========================")

def excluir_tarefa(id_tarefa):
    """Remove uma tarefa do banco pelo ID."""
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    
    # Verifica primeiro se o ID realmente existe
    cursor.execute("SELECT * FROM Tarefas WHERE id = ?", (id_tarefa,))
    if not cursor.fetchone():
        print(f"\n❌ Erro: Não existe nenhuma tarefa com o ID {id_tarefa}.")
    else:
        cursor.execute("DELETE FROM Tarefas WHERE id = ?", (id_tarefa,))
        conexao.commit()
        print(f"\n🗑️ Tarefa [{id_tarefa}] excluída/concluída!")
        
    conexao.close()

# --- MENU INTERATIVO DO SISTEMA ---
def menu():
    inicializar_banco()
    
    while True: #Nosso loop para gerenciar, parecido com o carrinho do projeto_burguer mas um pouco diferente... 
        print("\n--- 📝 GERENCIADOR DE TAREFAS SQLITE ---")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Excluir/Concluir Tarefa")
        print("4. Sair do Programa")
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            nova_tarefa = input("Digite a descrição da tarefa: ").strip()
            if nova_tarefa:
                adicionar_tarefa(nova_tarefa)
            else:
                print("❌ A descrição não pode ficar vazia.")
                
        elif opcao == "2":
            visualizar_tarefas()
            
        elif opcao == "3":
            visualizar_tarefas()
            try:
                id_para_deletar = int(input("Digite o ID da tarefa que deseja excluir: "))
                excluir_tarefa(id_para_deletar)
            except ValueError:
                print("❌ Erro: Por favor, digite um número de ID válido.")
                
        elif opcao == "4":
            print("\n👋 Saindo... Bom descanso e até a próxima aula!")
            break
        else:
            print("❌ Opção inválida! Digite um número de 1 a 4.")


menu()

#Com esse exemplo acho que podemos aprimorar o sistema de hamburgueria🤙🍃