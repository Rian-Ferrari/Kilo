from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
Socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mensagens
@Socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# criar rota
@app.route("/")
def homepage():
    return render_template("index.html")

# rodar o aplicativo web
Socketio.run(app, host="localhost")

# websocket -> tunel 