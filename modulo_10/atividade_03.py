''' Criando um sistema de timeout na API - tratando erros - '''

import requests


from requests.exceptions import HTTPError, ConnectionError, Timeout

def request_safe():
    url = "https://api.open-meteo.com/v1/forecast?latitude=-23.5505&longitude=-46.6333&current_weather=true"

    try:
        print(" TENTANDO CONECTAR À API...")
        # O argumento 'timeout=3' diz: se o servidor demorar mais de 3 segundos
        # para responder, desista e jogue um erro de Timeout.
        resposta = requests.get(url,timeout=3)

        # O raise_for_status() verifica se o servidor retornou um erro HTTP (ex: 404 ou 500)
        # Se retornou, ele dispara um HTTPError automaticamente
        resposta.raise_for_status()

        # Se passou direto, os dados estão ok!
        dados = resposta.json()
        print("\nDados recebidos com sucesso!")
    except ConnectionError:
        print("[ERRO DA REDE ⛓️‍💥]: Não foi possível conectar ao servidor. Verifique sua internet por favor...")

    except Timeout:
        print("[ERRO DE TEMPO 🐌]: O servidor demorou demais para responder (Conexão Lenta).")

    except HTTPError as erro_http:
        print(f"[ERRO HTTP 🖥️]: O servidor respondeu com um status de erro. Detalhes: {erro_http}")

    except Exception as outro_erro:
        print (f"Ocorreu um erro inesperado: {outro_erro}")


request_safe()