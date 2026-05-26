'''Criando uma calculadora mais "segura" podemos dizer - não vai dar encerrar o sistema quando der erro.'''
def calculadora_segura():
    try:
        # Pode dar erro se o usuário digitar uma letra
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Pode dar erro se o usuário digitar 0
        resultado = num1/num2

        print(f"O resultado da divisão é: {resultado}")
    except ZeroDivisionError:
        print("[Erro]: Você não pode dividir por zero!")
    except ValueError:
        print("[ERRO]: Por favor, digite apenas números válidos (letras não são permitidas!)")
    except Exception as erro_generico: # O "Exception" captura QUALQUER outro erro que a gente não previu
        print(f"Ocorreu um erro inesperado: {erro_generico}")
calculadora_segura()