def realizar_login (): #função realizar_login, onde não temos numeros de repetições e usando dois pontos : deve ser feito algo
 usuario = {}
    
    #Função que simula uma tela de login capturando nome e senha.
 print ('\n---- Tela de login ----\n')
 nome = input ('Digite seu nome para continuar: ').strip() .title()
 senha = input ('Digite a sua senha para continuar: ').strip() .title()
 
 usuario[nome] = senha

 print(f"Seja bem vindo(a), {nome}! Espero que você esteja bem!")
 print('-'*25)

realizar_login()
