''' Criando uma API de blog integrada com o SQLite'''

import os
import sqlite3
import webbrowser
from threading import Timer
from flask import Flask, jsonify, request

app = Flask(__name__)

# Configuração de caminhos
PATH_PASTA = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(PATH_PASTA, "banco_blog.db")

def inicializar_banco():
    """Cria as tabelas do blog caso não existam."""
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    # Tabela de Usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    );""")
    # Tabela de Posts
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        conteudo TEXT NOT NULL,
        autor TEXT NOT NULL
    );""")
    conexao.commit()
    conexao.close()

# ROTA 1: Cadastro de Usuários (Autenticação básica)
@app.route('/api/registrar', methods=['POST'])
def registrar():
    dados = request.get_json()
    if not dados or "username" not in dados or "senha" not in dados:
        return jsonify({"erro": "Informe 'username' e 'senha'."}), 400
    
    try:
        conexao = sqlite3.connect(DB_NAME)
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO Usuarios (username, senha) VALUES (?, ?)", (dados["username"], dados["senha"]))
        conexao.commit()
        conexao.close()
        return jsonify({"mensagem": f"Usuário {dados['username']} criado com sucesso!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"erro": "Este nome de usuário já existe."}), 400

# ROTA 2: Criar Novo Post do Blog
@app.route('/api/posts', methods=['POST'])
def criar_post():
    dados = request.get_json()
    if not dados or "titulo" not in dados or "conteudo" not in dados or "autor" not in dados:
        return jsonify({"erro": "Informe 'titulo', 'conteudo' e 'autor'."}), 400
        
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Posts (titulo, conteudo, autor) VALUES (?, ?, ?)", 
                   (dados["titulo"], dados["conteudo"], dados["autor"]))
    conexao.commit()
    conexao.close()
    return jsonify({"mensagem": "Post publicado com sucesso!"}), 201

# ROTA 3: Listar Todos os Posts (GET)
@app.route('/api/posts', methods=['GET'])
def listar_posts():
    conexao = sqlite3.connect(DB_NAME)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Posts")
    linhas = cursor.fetchall()
    conexao.close()
    
    lista_posts = []
    for l in linhas:
        lista_posts.append({"id": l[0], "titulo": l[1], "conteudo": l[2], "autor": l[3]})
        
    return jsonify(lista_posts), 200

# Rota Inicial Informativa
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "status": "API do Blog Rodando!",
        "rotas_disponiveis": [
            "POST /api/registrar (Cadastrar usuário)",
            "POST /api/posts (Criar post)",
            "GET /api/posts (Ver todos os posts)"
        ]
    }), 200

def abrir_navegador():
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == '__main__':
    inicializar_banco()
    Timer(1, abrir_navegador).start()
    app.run(debug=False)