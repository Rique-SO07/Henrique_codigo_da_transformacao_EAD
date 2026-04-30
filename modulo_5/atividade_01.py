def saudacao():
 print("\n ---- Tela de boas vindas ----")
 nome = {} #Dicionário pra salvar o nome

 nome = input("\n Olá, por favor digite o seu nome: ").strip() .title() #.title() Vai definir a primeira letra em maiúsculo sempre
 
 saudacao_user = nome .strip() .title()
 print(f"\nOlá, {saudacao_user} seja bem vindo(a)! Espero que você esteja bem! ")
saudacao()