'''Aqui vamos utilizar uma API da NASA que irá filtrar fotos astronômicas do dia..
   - Pois sem querer tranformei a ativ.1 na ativ.2 ao mesmo kk...'''

import requests

def obter_foto_nasa():
# URL da API pública da NASA (usando uma chave de demonstração "DEMO_KEY"
   url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

   try: 
     print(" \n CONECTANDO AOS SERVIDORES DA NASA...")
     resposta = requests.get(url)

      # Aqui vai transformar o json bruto em um dicionário Python
     dados_api = resposta.json()

     # Aqui nós escolhemos a dedo dentro daquele monte de tabela o que queremos exibir (Um parâmetro se não me engano.)
     titulo = dados_api.get("title","Sem título")
     data = dados_api.get("date", "Sem data")
     url_imagem = dados_api.get("url", "Sem link")

    # Pegamos apenas os primeiros 150 caracteres da explicação para não poluir o terminal
     explicacao = dados_api.get("explanation", "Sem explicação")
     #Cortando a string para exibir apenas um resumo deixa o layout do seu terminal sob controle.
     resumo_explicacao = explicacao [:150] + "..." 

     print("\n" + "="*50)
     print("🌌 --- DESCOBERTA ASTRONÔMICA DO DIA (NASA) --- ")
     print("="*50)
     print(f"{'📅 Data:':<15} {data}")
     print(f"{'🔭 Título:':<15} {titulo}")
     print(f"{'🔗 Link da Foto:':<15} {url_imagem}")
     print(f"{'📝 Resumo:':<15} {resumo_explicacao}")
     print("="*50)
        
   except Exception as erro:
        print(f"❌ Erro ao acessar a API da NASA: {erro}")

# Depois só preciso ver como posso deixar em português
obter_foto_nasa()