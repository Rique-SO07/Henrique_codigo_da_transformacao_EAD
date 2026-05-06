# Nossa 'Base de Dados' fixa para evitar erros de arquivo por enquanto
BASE_PRODUTOS = [
    {"nome": "Teclado", "preco": 150.00},
    {"nome": "Mouse", "preco": 120.00},
    {"nome": "Monitor", "preco": 850.00},
    {"nome": "Mousepad", "preco": 60.00}
]

def listar_produtos():
    print("\n" + "-"*30)
    print(f"{'PRODUTO':<15} | {'PREÇO':<10}")
    print("-"*30)
    for p in BASE_PRODUTOS:
        print(f"{p['nome']:<15} | R$ {p['preco']:>7.2f}")
    print("-"*30)

def buscar_produto(nome_busca):
    for p in BASE_PRODUTOS:
        if p['nome'].lower() == nome_busca.lower():
            return p
    return None