'''Criando um sistema de previsão do tempo utilizando uma API (Open-meteo)'''
import requests


def traduzir_clima(codigo_clima):
    '''Mapeando os códigos universais da API WMO para descrições em emojis (em pt-br)'''

    tabela_clima = {
        0:  ["☀️", "Céu Limpo / Ensolarado"],
        1:  ["🌤️", "Principalmente Limpo"],
        2:  ["Partially Cloudy", "Parcialmente Nublado"],
        3:  ["☁️", "Encoberto / Nublado"],
        45: ["🌫️", "Névoa / Neblina"],
        48: ["🌫️", "Neblina com Geada"],
        51: ["🌧️", "Chuva Leve / Chuvisco"],
        53: ["🌧️", "Chuva Moderada"],
        55: ["🌧️", "Chuva Intensa"],
        61: ["🌧️", "Chuva Fraca"],
        63: ["🌧️", "Chuva Moderada"],
        65: ["🌧️", "Chuva Forte"],
        71: ["❄️", "Queda de Neve Leve"],
        73: ["❄️", "Queda de Neve Moderada"],
        75: ["❄️", "Queda de Neve Forte"],
        80: ["🌦️", "Pancadas de Chuva Leves"],
        81: ["🌦️", "Pancadas de Chuva Moderadas"],
        82: ["⛈️", "Pancadas de Chuva Violentas"],
        95: ["⚡⛈️", "Tempestade / Trovoadas"],

    }
    return tabela_clima.get(codigo_clima, ["🌎", "Condição não encontrada"])

def obter_previsao():

    url = "https://api.open-meteo.com/v1/forecast?latitude=-23.5505&longitude=-46.6333&current_weather=true"

    try:
        print("Conectando ao servidor de clima...")
        resposta = requests.get(url)
        
        dados = resposta.json()

        clima_atual = dados["current_weather"]
        temperatura = clima_atual["temperature"]
        velocidade_vento = clima_atual["windspeed"]
        codigo_codicao = clima_atual["weathercode"]

        emoji, condicao_texto = traduzir_clima(codigo_codicao)

        print("\n --- PREVISÃO DO TEMPO (SÂO PAULO) ---")
        print("="*40)
        print(f"🌤️ Temperatura atual: {temperatura}°C")
        print(f"🍃 Velocidade do Vento: {velocidade_vento} km/h")
        print(f"{'Condição:':<20} {emoji} {condicao_texto}")
        print("="*40)
    except Exception as erro:
        print(f"[ERRO] falha ao obter dados: {erro}")
obter_previsao()