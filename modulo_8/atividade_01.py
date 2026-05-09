'''Criando uma Classe carro para exibir modelo, marca e modelo de ano'''

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):
        return f" {self.marca} {self.modelo} | Ano: {self.ano}"


meu_carro = Carro("Honda","Civic", 2008)
carro_do_carlos = Carro("Hyundai", "HB20", 2024)

print("Meu carro:", meu_carro.exibir_info())
print("Carro de Carlos:", carro_do_carlos.exibir_info())

#Posso utlizar este meio também:
'''meu_carro.exbir_info()
   carro_do_carlos.exibir_info()'''