def maior_menor(numeros):
    print("\n---- Acessando diferença de números maiores e menores ----")
   
    return max(numeros), min(numeros)


entrada = input("Digite vários números separados por espaço para verificar qual é menor e maior (Ex: 1 2 3 4 5...): ")


# O .split() quebra o texto nos espaços e cria uma lista
# [float(n) for n in ...] vai converter cada texto em número real
lista_numeros = [float(n) for n in entrada.split()]

maior, menor = maior_menor(lista_numeros)

print(f"Maior: {maior} | Menor: {menor}")
print("-"*25)
