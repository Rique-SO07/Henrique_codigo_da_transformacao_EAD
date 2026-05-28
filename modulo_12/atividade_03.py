'''Testando reações e entradas inválidas'''

import unittest 

#Função para validar os dados de cadastro do user
def cadastrar_user(nome, idade, email):
    if idade <18:
        raise ValueError("Apenas maiores de 18 anos podem se cadastrar. ☝️👴")
    if "@" not in email: 
        raise TypeError("O e-mail digitado é inválido.")
    
    return (f"Usuário {nome} cadastrado com sucesso!")


#Classe de teste focada em testar os "caminhos de erro"(Entradas inválidas)
class TesteValidacaoUser(unittest.TestCase):

    def test_cadastro_com_sucesso(self):
        """Valida se o cadastro funciona quando todos os dados estão corretos."""

        resultado = cadastrar_user("Fredão", 25, "fredaosheik@email.com")
        self.assertEqual(resultado, "Usuário Fredão cadastrado com sucesso!")

    def test_erro_idade_limit(self):
        """Garante que o sistema nega o cadastro de menores de 18 anos lançando ValueError."""

        # Se colocar idade 16, o sistema deve disparar um ValueError
        with self.assertRaises(ValueError):
            cadastrar_user("Joãozin Pimpolho", 15, "joaogamer@email.com" )

    def test_erro_email_arroba(self):
        """Garante que o sistema recusa e-mails inválidos lançando TypeError."""
        
        # Se o e-mail não tiver '@', o sistema deve disparar um TypeError
        with self.assertRaises(TypeError): 
            cadastrar_user("Carlão", 30, "carlos.email.com")

if __name__ == "__main__":
    unittest.main()