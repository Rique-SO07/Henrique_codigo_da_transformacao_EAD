'''Sistema multiplo sobre estrutura de dados e listas
- Muito provavelmente não foi o jeito mais certo de se fazer... '''



lista_compras = [] #Lista comum mutável e ordenada
aluno = {} # Dicionário (Chave:Valor), ele é  ideal para mapear propriedades de um objeto
contatos = {} # Dicionário, esse também é ideal para buscas rápidas por chave única (Nome)

while True:
    print("="*30)
    print("\nBoas vindas ao sistema de listas!\n")
    print("="*30)
    print("\nQue tal dar uma olhada nessas opções de listas?\n")
    print("[1] Lista de Snacks")
    print("[2] Dicionário de dados do aluno") 
    print("[3] Conjuntos de Pares e Ímpares ")
    print("[4] Agenda de contatos")
    print("[0] Sair do sistema")

    opcao = input("\nEscolha uma opção:").strip()


    if opcao == "0":
        print("Saindo do sistema... Até logo, aproveite o seu dia! ")
        break

    if opcao == "1": 
     print('\n Acessando a lista de Snacks...')
     print('\n---- Olá, fique a vontade para escolher o seu Snack!----')

    
     nome_item = ""
     total = 0

     while True:
      
         print(f"\nLista atual: {lista_compras}")
         print("\nMenu de Snacks:")
         print("[1] Tacos tradicionais (R$10.00)")
         print("[2] Bolinhos de arroz (R$13.60)")
         print("[3] Batata frita (R$15.00)")
         print("[4] Isca de frango (R$20.30)")
         print("[5] Remover último item")
         print("[0] Concluir e voltar ao Menu Principal")

         escolha_snack = input("\nO que deseja adicionar? ").strip()

         if escolha_snack == "0":
                print("Retornando ao menu principal...")
                break # Sai apenas do loop de compras da lista

         elif escolha_snack == "1":
                lista_compras.append("Tacos") # .append() adiciona um elemento ao final da lista
                print(">> Tacos adicionados!")
            
         elif escolha_snack == "2":
                lista_compras.append("Bolinhos de arroz")
                print(">> Bolinhos adicionados!")

         elif escolha_snack == "3":
                lista_compras.append("Batata frita")
                print(">> Batata frita adicionada!")

         elif escolha_snack == "4":
                lista_compras.append("Isca de frango")
                print(">> Isca de frango adicionada!")

         elif escolha_snack == "5":
                
                if lista_compras:
                    removido = lista_compras.pop() # .pop() remove e retorna o último item da lista
                    print(f">> {removido} foi removido.")
                else:
                    print(">> A lista está vazia!")
            
         else:
                print("Opção inválida dentro do carrinho.")





                           
    elif opcao == "2": # Atribuição direta de valores às chaves do dicionário
      print("\n ---- Dados do aluno ----")
      aluno["Nome"] = input("Digite o nome do aluno: ").strip()
      aluno["Idade"] = int(input("Digite a idade do aluno: "))
      aluno["Notas"] = [8.0, 9.5, 10.0, 8.5] #Lista aninhada dentro do dicionário

      print("\nExibindo detalhes sobre o aluno(a)...\n")
      print("\nExibindo detalhes:")
      for chave, valor in aluno.items(): # Aqui o .items() permite iterar simultaneamente sobre a Chave e o Valor
            print(f"{chave}: {valor}")
            print("-"*25)
    




    elif opcao == "3":
      print("\n ---- Acessando o conjunto de números pares e ímpares ----")
      limite = int(input("\nAté qual número deseja analisar?"))
      pares=[]
      impares=[]

      for i in range(1, limite +1): # O range(início, fim+1) gera a sequência numérica desejada
        #O Operador % (Módulo) verifica o resto da divisão. 
        if i % 2 == 0:  # Se o resto por 2 é 0, o número é par.
         pares.append(i)
        else:
         impares.append(i)
        
        print(f"\nPares identificados: >> {pares}")
        print(f"\nÍmpares identificados: >> {impares}")


    elif opcao == "4":
      print("\n Acessando a Agenda...\n")
      print("\n--- Agenda de Contatos ---")
      print("[1] Adicionar | [2] Remover | [3] Ver Todos")
      sub = input("Escolha: ")
        
      if sub == "1": #Variavel para o mini sistema de remoção e adição de contatos
            nome = input("Insira o nome do contato: ")
            tel = input("Insira o número de telefone: ")
            contatos [nome] = tel # Adição/Atualização: se a chave já existe, o valor é atualizado
            print({nome},"Foram adicionados!")
            print("-"*25)
            print("\tRetornando ao menu principal...\n")
            print("-"*25)

      elif sub == "2":
            
            nome_remover = input("Digite o nome do contato que deseja remover: ").strip()
            
            # Verificando se o nome existe no dicionário antes de deletar, além de ter adicionado uma variável para ficar mais fácil a remoção.  
            if nome_remover in contatos: # Busca de Chave: 'in' verifica se a chave existe dentro do meu dicionário, meio confuso
                confirmar = input(f"Tem certeza que deseja remover {nome_remover}? (S/N): ").upper()
                if confirmar == 'S':
                    del contatos[nome_remover] # o del remove a entrada completa (Chave e Valor) do dicionário
                    print(f"\n>> {nome_remover} foi removido da agenda.")
            else:
                print("\n>> Contato não encontrado!")
            
            
            
            
            
            '''if nome != "":                                                          - Jeito antigo que tinha feito, esqueci que é um dicionário e não uma lista.
                
                obs = input(f"Deseja remover {contatos}? (S/N): ").upper()
                detalhes = "Sem observações"
                if obs == 'S':
                    detalhes = input("Digite 'Sim' para confirmar: ")
                    del contatos[nome,tel] #Del vai deletar a minha lista de contatos
                print(f"\n{nome,tel} Foi removido...")

                contatos.append ({
                    "nome": nome,
                    "telefone": tel,
                    "obs": detalhes
                })
                
            else: print("Não encontrado.")'''


      elif sub == "3":
            if not contatos:
                print("\n>> A agenda está vazia!")
            else:
                print("\n--- Lista de Contatos ---")
                # Percorrendo o dicionário para exibir todos os contatos salvos dentro do dicionário
                for nome, telefone in contatos.items():
                    print(f"Nome: {nome} | Tel: {telefone}")
            
            print("-" * 25)
            print("\tRetornando ao menu principal...\n")
    
      elif sub == "4": #Aqui fiz uma alteração, consegui fazer uma ferramenta de buscar contatos já salvos, caso tenha muitos contatos. 
            nome_busca = input("Digite o nome que deseja procurar: ").strip()
            
            # O 'in' verifica se a chave existe no dicionário
            if nome_busca in contatos:
                # Se existir, acessamos o valor (telefone) usando a chave
                print(f"\n[SUCESSO] Contato encontrado:")
                print(f"Nome: {nome_busca}")
                print(f"Telefone: {contatos[nome_busca]}")
            else:
                print(f"\n[AVISO] O contato '{nome_busca}' não está na sua agenda.")
            
            print("-" * 25)
            print("\tRetornando ao menu principal...\n")
    else:
      print("Opção inválida, tente novamente!")