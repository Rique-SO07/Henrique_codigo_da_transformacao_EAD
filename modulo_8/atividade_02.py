class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):
        print(f"{self.marca} {self.modelo} | Ano: {self.ano}")
    

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano, autonomia_bateria, recarga):
        super().__init__(marca, modelo, ano)# o comando super() chama o construtor da classe pai (Carro)
        #Assim não preciso reescrever self.marca = marca, entre outros. 

        #Como dito anteriormente, agora é só focar nas classes novas
        self.autonomia_bateria = autonomia_bateria
        self.recarga = recarga


    def exibir_info_eletrico(self):
       self.exibir_info()
       print(f"A autonomia da Bateria: {self.autonomia_bateria} km")
       print(f"O tempo de Recarga é apróx.: {self.recarga} min.")

meu_byd = CarroEletrico("BYD","Dolphin Mini", 2025, 280, 40)
meu_byd.exibir_info_eletrico()