import webbrowser
from threading import Timer
from flask import Flask, jsonify, request

app = Flask(__name__)

# Rota POST para receber os dados de cadastro
@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    # Coleta o JSON enviado no corpo (body) da requisição
    dados = request.get_json()
    
    # Validação simples para não aceitar dados vazios
    if not dados or "nome" not in dados or "email" not in dados:
        return jsonify({"erro": "Dados inválidos! Forneça 'nome' e 'email'."}), 400
        
    nome = dados["nome"]
    email = dados["email"]
    
    # Simula a resposta de sucesso do cadastro
    return jsonify({
        "status": "Sucesso",
        "mensagem": f"Usuário {nome} cadastrado com sucesso com o e-mail {email}!"
    }), 201


# Rota GET apenas para te dar instruções na tela ao abrir o navegador
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "mensagem": "Servidor de cadastro rodando!",
        "instrucao": "Como rotas POST não podem ser testadas direto digitando no navegador, use o Postman, Insomnia ou execute o teste automático."
    }), 200

def abrir_navegador():
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == '__main__':
    Timer(1, abrir_navegador).start()
    app.run(debug=False)