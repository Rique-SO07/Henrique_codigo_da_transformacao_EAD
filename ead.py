''' Minha primeira calculadora média em python, com histórico e opção de continuar a operar com o resultado anterior. Bem bosta.
'''


print('\n--- Calculadora média pra bocós que nem eu kkkkkk---')

historico = []
resultado_atual = None  # Guarda o último resultado para continuar operando com resultado anterior

while True:
    print("\n[ MENU PRINCIPAL ]")
    print("1. Novo Cálculo")
    print("2. Ver Histórico")
    print("3. Usar último resultado para nova operação")
    print("s. Sair")
    
    escolha = input("\nEscolha uma opção: ").lower()

    if escolha == 's':
        break

    # --- OPÇÃO 1: NOVO CÁLCULO ---
    if escolha == '1':
        num_um = float(input('Digite o primeiro número: '))
        num_dois = float(input('Digite o segundo número: '))
        op = input('Operação (+, -, *, /): ')
        
        # Processamento simplificado
        if op == '+': res = num_um + num_dois
        elif op == '-': res = num_um - num_dois
        elif op == '*': res = num_um * num_dois
        elif op == '/': res = num_um / num_dois if num_dois != 0 else "Erro"
        
        if res != "Erro":
            resultado_atual = res # Salva para a Opção 3
            frase = f"{num_um} {op} {num_dois} = {res}"
            historico.append(frase)
            print(f"\n-> Deu essa bomba ae ó: {res}")
        else:
            print("\nERRO: Divisão por zero!")

    # --- OPÇÃO 2: VER HISTÓRICO ---
    elif escolha == '2':
        print("\n--- HISTÓRICO ---")
        if not historico:
            print("Vazio.")
        for i, item in enumerate(historico):
            print(f"{i+1}. {item}")
        input("\nPressione Enter para voltar ao menu zé...")

    # --- OPÇÃO 3: CONTINUAR OPERANDO ---
    elif escolha == '3':
        if resultado_atual is None:
            print("\nNenhum resultado anterior encontrado!")
        else:
            print(f"\nValor atual: {resultado_atual}")
            op = input('Qual operação deseja aplicar a esse valor? (+, -, *, /): ')
            num_novo = float(input(f'Digite o número para aplicar a {resultado_atual}: '))
            
            valor_antigo = resultado_atual # Guarda para o texto do histórico
            
            if op == '+': resultado_atual += num_novo
            elif op == '-': resultado_atual -= num_novo
            elif op == '*': resultado_atual *= num_novo
            elif op == '/': 
                if num_novo != 0: resultado_atual /= num_novo
                else: print("Erro: Divisão por zero! Nada a ver 🤡"); continue

            frase = f"{valor_antigo} {op} {num_novo} = {resultado_atual}"
            historico.append(frase)
            print(f"\n-> Novo Resultado: {resultado_atual}")

    else:
        print("Opção inválida! Vai agora bate palma pra maluco dançar")