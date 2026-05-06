from produtos.estoque import buscar_produto, listar_produtos
from financeiro.impostos import calcular_icms

def menu():
    print("\n" + "="*40)
    print(" LOJA DE PERIFÉRICOS ")
    print("="*40)
    
    listar_produtos()

    while True:
        print("\n[Comandos: 'lista' | 'sair']")
        opcao = input("Digite o nome do produto: ").strip()

        if opcao.lower() == 'sair':
            print("Encerrando... Bom descanso e bom apetite!")
            break
        
        if opcao.lower() == 'lista':
            listar_produtos()
            continue

        produto = buscar_produto(opcao)

        if produto:
            valor_imposto = calcular_icms(produto['preco'])
            total = produto['preco'] + valor_imposto
            
            print(f"\n {produto['nome']} encontrado!")
            print(f" Preço Base: R$ {produto['preco']:.2f}")
            print(f" Imposto (18%): R$ {valor_imposto:.2f}")
            print(f" Total: R$ {total:.2f}")
        else:
            print(f" Item '{opcao}' não encontrado.")

if __name__ == "__main__":
    menu()