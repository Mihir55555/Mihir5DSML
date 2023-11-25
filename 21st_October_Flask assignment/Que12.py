## 12. Build a Flask app that updates data in real-time using WebSocket connections.

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)

counter = 0
counter_lock = threading.Lock()

def background_thread():
    global counter
    while True:
        time.sleep(1)
        with counter_lock:
            counter += 1
            socketio.emit('update_counter', {'counter': counter}, namespace='/test')

@app.route('/')
def index():
    return render_template('websocket12.html')

@socketio.on('connect', namespace='/test')
def handle_connect():
    print('Client connected')
    with counter_lock:
        emit('update_counter', {'counter': counter})

@socketio.on('start_background_thread', namespace='/test')
def start_background_thread():
    print('Starting background thread')
    threading.Thread(target=background_thread, daemon=True).start()

if __name__ == '__main__':
    socketio.run(app,host="0.0.0.0",port=5002)