import socket
from flask_socketio import SocketIO, emit
from flask import Flask, render_template

app = Flask(__name__)

socket_io = SocketIO(app)


@socket_io.on('connect')
def printsocket():
    print("Connected")
    # emit('connection', "Established socket connection for connect")


@socket_io.on('button_clicked')
def buttonclicked(data):
    print(data['name'])


@app.route("/", methods=["GET", "POST"])
def hello():
    hi = "Hello"
    return render_template('index.html', msg=hi)


if __name__ == "__main__":
    socket_io.run(app)
