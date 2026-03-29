''' Aqui eu fiz um sistema básico de loop e múltiplas escolhas para as 3 opções básicas de estruturas de sistema 
(categorizações, Operações e Comparações)...🫠😢
'''


while True:
    print("-" * 23)
    print("Olá seja bem vindo ao menu de Calculo, operadores e classificações!")
    print("\n[1] Categorização de idades ")
    print("[2] Operações Aritiméticas ")
    print("[3] Comparações de números simples ")
    print("[0] Sair do Menu")
    print("-" * 23)

    escolha = input("\nEscolha uma opção: ").strip()

    if escolha == "0":
        print("\nSaindo do Menu... até mais!")
        break

    if escolha == "1":
        print("\nAcessando Categorização de idades...\n")

        idade = int(input("Digite a sua idade: "))

        if idade <=11: #Menor ou igual a 11 é criança
         print("Você É CRIANÇA! Vai desenhar sei lá 🙄 ")

        elif idade <=19: #Menor ou igual a 19 é adolescente
         print("Você é um adolescente! Sai desse celular! 🫠🤳")

        elif idade <= 60: #Menor que 60 ou igual a 60 é idoso
         print("Você é ~CLT~ quer dizer *ADULTO🤡 ")

        else:
         print("Você idoso!😎🤙 ")
        
     
    elif escolha == "2":
        print("\nAcessando as operações aritiméticas (calculadora básica)\n")

        num_um = float(input('Digite o primeiro número: '))
        num_dois = float(input('Digite o segundo número: '))
        op = input('Operação (+, -, *, /, %): ')

        #Calculadora com estrutura mais simples 
        if op == "+":   res = num_um + num_dois
        elif op == "-": res = num_um - num_dois
        elif op == "*": res = num_um * num_dois
        elif op == "/": 
           res = num_um / num_dois if num_dois != 0 else "Erro"
        elif op == "%": res = num_um % num_dois

        if res != "Erro":
            resultado_atual = res  # Variável para as respostas salvas  
            print(f"\n-> Resultado: {res}")
            
        else:
            print("\tERRO: Divisão por zero!")
            # \t faz a mensagem ir para o centro da linha


    elif escolha == "3":
        print("\nAcessando Comparações de números simples...\n")
        num_um = int(input("Digite o primeiro número: "))
        num_dois = int(input("Digite o segundo número: "))

        if num_um > num_dois:
         print(f"\nO valor {num_um} é maior que {num_dois}.\n ")

        elif num_dois > num_um:
         print(f"\nO valor {num_dois} é maior! que {num_um}. \n")
         print("-" * 30)
       
