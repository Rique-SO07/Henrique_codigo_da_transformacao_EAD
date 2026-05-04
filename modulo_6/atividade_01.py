#Criando um sistema para ler um arquivo 

with open('arquivo_loko.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("Isso é um teste, espero que dê certo! \n")
    arquivo.write("Eu estava pensando, um pouco preso no Oblívio")
    print("Arquivo criado e informações gravadas com sucesso!")


#Agora vou criar a forma de ler o arquivo. <--- pq eu falo assim ??

with open('arquivo_loko.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print("\n--- Conteúdo lido do arquivo ---\n", "-"*60)
    print(conteudo)