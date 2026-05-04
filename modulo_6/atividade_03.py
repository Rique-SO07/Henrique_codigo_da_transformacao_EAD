import csv

# Aqui irei criar uma lista de listas (confuso né?) é uma lista de notas de alunos
# Com "base" em algumas matérias em setores (ficticio)

notas_alunos = [
    ["Nome", "Matéria", "Nota"],
    ["Laís", "JavaScript", "10.0"],
    ["Laura", "Python", "8.5"],
    ["Fred", "Banco de Dados", "7.5"],
]

with open("notas_alunos.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(notas_alunos)
    # writerows escreve várias lnhas de uma vez, okay?
    # writerows (com 's' no final) serve para gravar a lista inteira
    print("Arquivo notas de alunos.csv criado com maestria!")


    ''' DICA: writerow (Singular): Espera uma lista simples (uma linha só). 
       Se você passa uma lista de listas, ele tenta espremer tudo em
       uma única linha do Excel, o que bagunça as colunas.

    writerows (Plural): Este é o correto para o seu caso! Ele percorre sua lista de listas 
    e escreve cada sub-lista em uma linha separada do arquivo.'''


print("\n--- Lendo o seu arquivo CSV ---")
with open("notas_alunos.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)

    # Verificamos se a linha tem exatamente 3 itens
    for linha in leitor: 
        if len(linha) == 3:
            nome, materia, nota = linha
            print(
                f"Aluno: {nome.ljust(10)} | Matéria: {materia.ljust(15)}| Nota: {nota}"
            )
        else:
            # Isso ignora linhas vazias ou com erro de formatação

            continue
