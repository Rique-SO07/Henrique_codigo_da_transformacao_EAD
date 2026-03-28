#---------- Sistema básico de boas vindas utilizando o datetime------------ 
from datetime import datetime #Importação do datetime para aplicar as horas

agora =  datetime.now() # Aqui vai capturar a hora atual do sistema
hora_formatada = agora.strftime("%H:%M") #Aqui iremos formatar as "Horas" e "Minutos", Exemplo:(14:43)

print("Olá, seja bem vindo(a)!")
nome = input (f"Digite o seu nome: " )
print(f"Boas vindas {nome}! O login foi efetuado com sucesso! 🤩👍...............[Enviado às {hora_formatada}]")