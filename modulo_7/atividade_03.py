import random
import math


def jogar():
    print("\n--- HHAHAHA BEM VINDO AO DESAFIO DE ADIVINHAÇÃO （￣︶￣）↗---\n")
    print("\n -Estou pensando em um número de 1 e 100... (👉ﾟヮﾟ)👉")
    print("=" * 70)

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    '''utilizando um tratamento de erro para rodar o código sem preocupação...'''
    while not acertou:
        try:
            palpite = int(input("\nQual o seu palpite caro jogador?? "))
            tentativas += 1

            # Calculando a distância usando math.fabs(valor absoluto)
            # Isso ajuda a dizer o quão longe está o jogador, sem sinal negativo.

            distancia = math.fabs(numero_secreto - palpite)

            if palpite == numero_secreto:
                print(f"\nPARABÉNS! Você acertou em {tentativas} tentativas! >.<")
                print("=" * 70)
                acertou = True

            elif palpite < numero_secreto:
                print("\nMais alto... HAHAHA〜(￣▽￣〜)")

            else:
                print("\nHmmm é mais baixo... (〜￣▽￣)〜")

            if not acertou and distancia <= 5:
                print(
                    "\nDIOS MIO, TÁ FERVENDO! Você está a menos de 5 números de distância! ...(*￣０￣)ノ"
                )
            elif not acertou and distancia <= 15:
                print("\n MAS ESTÁ QUEEEEENTE! (～o￣3￣)～")

        except ValueError:
            print("\nPor favor, jovem gafanhoto, apenas números inteiros!（*゜ー゜*）")
            # vai verificar se o jogador não colocou algo que não seja Int


# iniciar o jogo
if __name__ == "__main__":
    jogar()


