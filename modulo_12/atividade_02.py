import unittest


# A classe real com as regras de negócio
class Calculadora:
    def somar(self,a, b): 
        return a + b
    
    def dividir (self, a, b):
        if b == 0: 
            raise ValueError("Não é possível dividir por zero zé!")
        
        return a / b 
    
# A classe que automatiza os testes
class TesteCalculadora(unittest.TestCase):
    #O método setUp roda AUTOMATICAMENTE antes de cada teste.
    # Serve para não precisarmos ficar criando a calculadora em todo método.

    def setUp(self): # Cria a calculadora antes de cada teste rodar com a ajuda do setUp
        self.calc = Calculadora()

    def test_soma_valores(self):

        self.assertEqual(self.calc.somar(10,5), 15)
        self.assertEqual(self.calc.somar(-1,1),0)

    def test_divisao_valida(self):
        self.assertEqual (self.calc.dividir(10,2),5.0)
        self.assertEqual (self.calc.dividir(5,2),2.5)

        # O self.assertRaises verifica se o bloco abaixo REALMENTE joga um ValueError
        with self.assertRaises(ValueError):
            self.calc.dividir(10,0)

if __name__ == "__main__":
    unittest.main()