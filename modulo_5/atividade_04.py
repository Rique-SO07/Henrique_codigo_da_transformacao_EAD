def calcular_media_lista(notas):
    print("\n---- Acessando a média do aluno ----")
    # A função sum() soma todos os itens da lista
    # A função len() conta quantos itens existem
    media = sum(notas) / len(notas)
    
    status = "Aprovado meu fi" if media >= 7 else "Reprovado zé"
    return media, status

# lista sobre as notas já predefinidas
minhas_notas = [8.5, 7.0, 9.0, 6.5]
resultado, situacao = calcular_media_lista(minhas_notas)

print(f"\n Sua média Final: {resultado:.2f} | Seu status atual meu jovem: {situacao}")

#Essa é a "lista" de média, não tenho certeza se era pra fazer assim exatamente. Na verdade tudo.