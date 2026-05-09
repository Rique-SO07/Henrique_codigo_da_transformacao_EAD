class Filme:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano


    def __str__(self):
     return f"Filme: {self.titulo}| Feito por: {self.autor} de {self.ano}"


filme = Filme("Interestellar", "Critopher Nolan", 2014)
print(filme)
