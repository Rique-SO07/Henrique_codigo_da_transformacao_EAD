'''Criando um sistema de biblioteca com classes de livros e gerenciamento de empréstimos'''

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponivel" if self.disponivel else "Emprestado"
        # Variáveis separadas para não confundir o Python
        return f"{self.titulo:<20} | Autor: {self.autor:<15}[{status}]"
        # :<20 reserva 20 caracteres e alinha à esquerda para criar colunas alinhadas


class Biblioteca:
    def __init__(self):
        self.acervo = [] # Lista que guardará objetos da classe Livro

    def adicionar_livro(self, livro):
        self.acervo.append(livro)
        print(f"O Livro '{livro.titulo}' foi adicionado ao acervo.")

    def listar_livros(self):
        print("-"*70)
        print("\n --- Acervo da Biblioteca --- \n ")
        print("-"*70)
        for livro in self.acervo:
            print(livro)

    def emprestar_livro(self, titulo_procurado):
        for livro in self.acervo:
            if livro.titulo.lower() == titulo_procurado.lower():  # Isso seria um exemplo de polimorfismo
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"\nEmpréstimo de '{livro.titulo}' foi realizado!")
                    return # Sai da função após o sucesso
                else:
                    print(f"\nO livro '{livro.titulo}' já está emprestado!")
                    return # Sai da função se já estiver emprestado
                
        # Se o loop acabar e não der nenhum 'return', o livro não existe
        print(f"\nO Livro '{titulo_procurado} não foi encontrado no acervo. ")
        print("-"*70)



#Fazendo isso vamos Instânciar
biblioteca_municipal = Biblioteca()
l1 = Livro("Dom Quixote", "Miguel de Cerventes")
l2 = Livro("O pequeno principe", "Antoine de Saint-Exupéry")
l3 = Livro("Verity", "Collen Hoover")
l4 = Livro("O alienista", "Machado de Assis")

biblioteca_municipal.adicionar_livro(l1)
biblioteca_municipal.adicionar_livro(l2)
biblioteca_municipal.adicionar_livro(l3)
biblioteca_municipal.adicionar_livro(l4)

#biblioteca_municipal.listar_livros()
biblioteca_municipal.emprestar_livro("O pequeno principe")
biblioteca_municipal.emprestar_livro("O pequeno principe")

biblioteca_municipal.listar_livros()
print("-"*70)

