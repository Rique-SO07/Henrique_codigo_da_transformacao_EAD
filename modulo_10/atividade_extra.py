''' Criando um buscador de filmes com tratamento de erro e timeout na API.'''
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout

def buscar_filme_real():
    # minha chave API (ÓBVIAMENTE NÃO VOU DEIXAR ISSO AQUI NO FUTURO)
    MINHA_API_KEY = "d924449b319a2c877cfdb09eaa18617e"
    
    # Aqui vamos buscar a ID do filme que aparece no site
    id_filme = "1083381"
    
    # URL real do TMDB (repare no 'api_key=' no final e no '&language=pt-BR' para vir em português!)
    url = f"https://api.themoviedb.org/3/movie/{id_filme}?api_key={MINHA_API_KEY}&language=pt-BR"
    
    try:
        print("🎬 Conectando à API REAL do TMDB...")
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        
        dados_filme = resposta.json()
        
        # O resto do nosso código de filtragem continua igual:
        titulo = dados_filme.get("title", "Título Indisponível")
        sinopse = dados_filme.get("overview", "Sem sinopse disponível.")
        nota = dados_filme.get("vote_average", "N/A")
        ano_lancamento = dados_filme.get("release_date", "0000")[:4]
        
        print("\n" + "="*60) #fica mais estiloso vou adotar isso.
        print(f"📌 Título: {titulo} ({ano_lancamento})")
        print(f"⭐ Nota TMDB: {nota}/10")
        print(f"📝 Sinopse: {sinopse}")
        print("═"*60)
        
    except Exception as erro:
        print(f"⚠️ [Erro]: {erro}")

buscar_filme_real()