def pedir_idade():
    while True:
        try:
            # Tenta converter a entrada para inteiro
            idade =int(input("Digite a sua Idade: "))

            # Validação lógica: idade não pode ser negativa ou zero
            if idade <= 0:
                print("Erro: A idade deve ser um número positivo e maior que zero! EEERRR...🤨")
                continue
            return idade # Se chegou aqui, a idade é válida ou seja, Sai do loop.
        
        except ValueError:

            # Captura o erro caso o usuário digite letras ou números com vírgula
            print("Erro: Por favor, digite um número INTEIRO válido zé...")

def pedir_altura():
    while True: 
        try:
            # Tenta converter para float
            altura = float(input("Digite a sua altura em metros (ex: 1.75): "))
            if altura <=0 or altura > 2.00: # Sinto muito quem joga basquete, mas vai ficar pra próxima
                print("Erro: Altura inválida. Digite um valor real positivo e realista né...")
                continue
            return altura
        except ValueError:
            print("Erro: Use ponto(.) em vez de vírgula e digite apenas números.")

print("\n ---- SISTEMA DE MEDIÇÃO 1000% SEGURO ---")
nome = input("Digite seu nome: ").strip()
idade_validada = pedir_idade()
altura_validada = pedir_altura()

print("\n --- MEDIÇÃO REALIZADA COM SUCESSO ---")
print(f"Nome:{nome}")
print(f"Idade: {idade_validada} anos")
print(f"Altura: {altura_validada}m")