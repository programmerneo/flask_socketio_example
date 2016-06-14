from flask import Flask, render_template
from flask_socketio import SocketIO

import time
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

#  you socketio EMIT back to a JS function with a socket ON by the same name


@app.route('/')
def index():
    t = Thread(target=background_stuff)
    t.start()
    return render_template('index.html')

@socketio.on('value changed')
def value_changede(message):
    print(message['data'])
    socketio.emit('update value', message)

@socketio.on('connect')
def test_connect():
    print 'Connected'
    socketio.send('Connected')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

def background_stuff():
     print 'In background_stuff'
     while True:
         time.sleep(1)
         t = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
         print t
         socketio.emit('the time', {'time': t})

if __name__ == '__main__':
    socketio.run(app)