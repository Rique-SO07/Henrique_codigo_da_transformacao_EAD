'''Criando uma rota para um servidor em flask (no caso automatizada)'''
import webbrowser # Mão na roda para rodar o site e automatizar a URL
from threading import Timer #Um timer para subir o site
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/saudacao', methods=['GET'])
def saudar():
    return jsonify({"mensagem": "Olá! Seja bem-vindo à API Flask!"}), 200

def abrir_navegador():
    """Força o navegador a abrir direto na rota correta."""
    webbrowser.open("http://127.0.0.1:5000/saudacao")

if __name__ == '__main__':
    # Aguarda 1 segundo para o servidor subir e chama a função de abrir o navegador
    Timer(1, abrir_navegador).start()
    
    # Roda o servidor (com o debug=False para não abrir o navegador duas vezes)
    app.run(debug=False)