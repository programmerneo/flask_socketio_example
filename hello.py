from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

#  you socketio EMIT back to a JS function with a socket ON by the same name


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('value changed')
def value_changede(message):
    print(message['data'])
    socketio.emit('update value', message, broadcast=True)

@socketio.on('connect')
def test_connect():
    print 'Connected'
    socketio.send('Connected')

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)