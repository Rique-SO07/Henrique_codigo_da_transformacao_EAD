import json

# Lista para armazenar os dados na memória do programa
clientes = []

def adicionar_cliente(nome, idade, cidade):
    # Adiciona o novo dicionário à lista
    clientes.append({"nome": nome, "idade": idade, "cidade": cidade})
    
    # Salva a lista inteira atualizada no arquivo
    with open("clientes.json", "w", encoding="utf-8") as arquivo:
        json.dump(clientes, arquivo, indent=4, ensure_ascii=False)
    print(f"Cliente {nome} adicionado com sucesso!")

# Chamando a função
adicionar_cliente("Maria", 25, "São Paulo")
adicionar_cliente("João", 30, "Rio de Janeiro")

# Lendo e exibindo o arquivo JSON
print("\n--- Conteúdo do arquivo em JSON ---")
with open("clientes.json", "r", encoding="utf-8") as arquivo:
    dados_carregados = json.load(arquivo)
    print(dados_carregados)