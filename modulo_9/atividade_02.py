'''Criando uma simulação de conta bancária'''

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_saque):
        self.valor_saque = valor_saque
        self.saldo = saldo_atual
        # Passamos uma mensagem padrão para a classe Pai (Exception)
        super().__init__(f"Tentativa de saque de R${valor_saque:.2f} negada. | Saldo atual: R$ {self.saldo:.2f}")

class ContaBancaria: # Criando a classe que usa o nosso erro
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def sacar (self, valor):
        print(f"\n Tentando sacar R$ {valor:.2f} da conta de {self.titular}...") 
        if valor > self.saldo:
           # Se o valor for maior que o saldo, nós FORÇAMOS o erro a acontecer
           raise SaldoInsuficienteError(self.saldo,valor)
        self.saldo -= valor
        print(f"Saque realizado com sucesso! Saldo atual: R$ {self.saldo:.2f}")

minha_conta = ContaBancaria("Henrique", 900.00)

try:
    minha_conta.sacar(200.00) # Esse vai dar certo
    minha_conta.sacar(400.00) # Esse vai estourar o saldo e disparar o erro

except SaldoInsuficienteError as erro:

    # Aqui Capturamos a nossa exceção customizada e tratamos ela aqui
    print(f"Operação Bloqueada!")
    print(f"Detalhes do erro: {erro}")

print("\n O sistema do banco continuou rodando com segurança.")