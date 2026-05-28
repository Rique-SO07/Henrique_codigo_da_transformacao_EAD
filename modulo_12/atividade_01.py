'''Vamos fazer um teste de soma utilizando o unittest (sem o input '''
import unittest

def somar(a,b): 
    return a + b

# A classe de testes que herda de unittest.TestCase
class TesteFuncaoSoma(unittest.TestCase):

    # Cada método de teste DEVE começar obrigatoriamente com a palavra 'test_'
    def test_soma_num_positivos(self):
        '''Testa se a soma de dois números positivos funciona'''
        resultado = somar(5,7)
        #Aqui esperamos que 5 + 7 seja igual a 12
        self.assertEqual(resultado,12) # Se eu colocar o resultado errado, ele informa

    def test_soma_num_negativos(self):
        '''Testa se a soma de números negativos funciona corretamente'''
        resultado = somar(-3,-2)

        self.assertEqual(resultado,-5)
        # Esperamos que -3 + (-2) seja igual a -5
    def test_soma_com_zero(self):
        """Testa se a soma com zero mantém o valor do outro número."""
        self.assertEqual(somar(10,0),10)

# Aqui executamos os testes quando rodamos o arquivo diretamente
if __name__ == "__main__":
    unittest.main()