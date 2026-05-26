''' Criando um sistema de login com credenciais inválidas'''

class CredenciaisInvalidasError(Exception): #Criando uma exceção personalizada.
    def __init__(self, tentativas_restantes):
        self.tentativas_restantes = tentativas_restantes
        super().__init__(f"Usuário ou senha incorretos! Tentativas restantes: {tentativas_restantes}")

def realizar_login(): # Função que valida o login e gerencia o erro
    #Aqui é um mini "banco de dados" de usuário cadastrado
    USUARIO_CORRETO = "admin"
    SENHA_CORRETA = "1234"
    tentativas = 3

    print(" --- SISTEMA DE LOGIN DE SEGURANÇA ---")

    while tentativas > 0:
        try:
            usuario = input("\nUsuário:").strip()
            senha = input("\nSenha: ").strip()
            
            # Se os dados estiverem corretos, faz o login e quebra o loop
            if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
                print("\n Acesso concedido! Bem-vindo(a) ao sistema!")
                return True
            
            # Se errou, reduz uma tentativa e lança o erro de propósito
            tentativas -= 1
            raise CredenciaisInvalidasError(tentativas)
        
        # O except captura o erro que nós mesmos lançamos e exibe a mensagem amigável
        except CredenciaisInvalidasError as erro:
            print(f"Erro de autenticação: {erro}")

            if tentativas == 0:
                print("\n CONTA BLOQUEADA ZÉ! Você esgotou as suas 3 tentativas. Procure o suporte esquecido ")
realizar_login()