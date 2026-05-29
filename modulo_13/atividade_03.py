'''Integrando o flask com o SQLite'''

import os
import sqlite3
import webbrowser
from threading import Timer
from flask import Flask, jsonify, request

app = Flask(__name__)

# Configuração de caminhos para o banco de dados
PATH_PASTA = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(PATH_PASTA, "banco_api.db")

def inicializar_banco():
    """Cria o banco de dados e a tabela caso não existam."""
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    );
    """)
    conexao.commit()
    conexao.close()

# Rota POST para receber JSON e gravar no SQLite
@app.route('/cadastrar', methods=['POST'])
def cadastrar_no_banco():
    dados = request.get_json()
    
    if not dados or "nome" not in dados or "email" not in dados:
        return jsonify({"erro": "Dados inválidos! Forneça 'nome' e 'email'."}), 400
        
    nome = dados["nome"]
    email = dados["email"]
    
    try:
        # Abre a conexão, insere o usuário e fecha
        conexao = sqlite3.connect(DB_NAME)
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO Usuarios (nome, email) VALUES (?, ?)", (nome, email))
        conexao.commit()
        conexao.close()
        
        return jsonify({
            "status": "Sucesso",
            "mensagem": f"Usuário {nome} gravado com sucesso no SQLite!"
        }), 201
        
    except sqlite3.IntegrityError:
        return jsonify({"erro": "Este e-mail já está cadastrado no banco."}), 400


# Rota GET apenas para testar no navegador e ver se o servidor está ativo
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "status": "Servidor integrado com SQLite rodando!",
        "banco_de_dados": "banco_api.db criado com sucesso na pasta."
    }), 200

def abrir_navegador():
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == '__main__':
    # Inicializa a tabela antes de subir o servidor
    inicializar_banco()
    
    Timer(1, abrir_navegador).start()
    app.run(debug=False)