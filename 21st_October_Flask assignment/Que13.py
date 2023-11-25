##  13.Implement notifications in a Flask app using websockets to notify users of updates.

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('update13.html')

@socketio.on('message')
def handle_message(msg):
    print('Message received: ', msg)
    socketio.emit('notification', {'data': 'New notification: ' + msg}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0",port=5001)