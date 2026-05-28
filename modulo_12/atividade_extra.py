'''API FLASK COM LÓGICA DE RECOMENDAÇÃO AUTOMATIZADA'''

import pytest
from flask import Flask, jsonify, request




app = Flask(__name__)

# Nosso pequeno banco de dados de séries e recomendações
BASE_SERIES = {
    "ruptura": {"genero": "Ficção Científica / Suspense", "recomendacao": "Black Mirror"},
    "dark": {"genero": "Ficção Científica / Mistério", "recomendacao": "1899"},
    "the office": {"genero": "Comédia", "recomendacao": "Parks and Recreation"}
}

@app.route('/api/recomendar', methods=['GET'])
def recomendar_serie():
    """Rota automatizada. O usuário passa ?gosto_de=nome_da_serie na URL
    e a API decide o que responder."""
    # Pega o parâmetro enviado na URL e transforma em minúsculo
    nome_serie = request.args.get('gosto_de', '').lower().strip()
    
    if not nome_serie:
        return jsonify({"erro": "Você precisa informar o parâmetro 'gosto_de'!"}), 400

    if nome_serie in BASE_SERIES:
        dados = BASE_SERIES[nome_serie]
        return jsonify({
            "sua_serie": nome_serie.title(),
            "genero": dados["genero"],
            "se_gostou_desse_vai_adorar": dados["recomendacao"]
        }), 200
    else:
        return jsonify({"erro": f"Ainda não temos recomendações para '{nome_serie}'."}), 404



# AMBIENTE DE TESTES (PYTEST FIXTURE)

@pytest.fixture
def cliente():
    app.config['TESTING'] = True
    with app.test_client() as cliente_teste:
        yield cliente_teste



# AUTOMATIZAÇÃO DOS TESTES

def test_recomendacao_para_ruptura_sucesso(cliente):
    """Testa se a API recomenda corretamente algo para quem gosta de Ruptura."""
    # Fazemos um GET passando o parâmetro na URL (?gosto_de=ruptura)
    resposta = cliente.get('/api/recomendar?gosto_de=ruptura')
    dados = resposta.get_json()
    
    assert resposta.status_code == 200
    assert dados["se_gostou_desse_vai_adorar"] == "Black Mirror"

def test_recomendacao_serie_inexistente_erro(cliente):
    """Testa se a API reage corretamente (404) quando a série não está no banco."""
    resposta = cliente.get('/api/recomendar?gosto_de=chaves')
    dados = resposta.get_json()
    
    # Esperamos um erro 404 (Not Found) e a mensagem de erro tratada
    assert resposta.status_code == 404
    assert "Ainda não temos recomendações" in dados["erro"]

def test_requisicao_sem_parametro_erro(cliente):
    """Testa se o sistema barra requisições que vêm sem nenhuma série informada."""
    resposta = cliente.get('/api/recomendar') # Sem nenhum parâmetro
    assert resposta.status_code == 400