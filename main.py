from flask import Flask
from flask import request, render_template
from flask_socketio import SocketIO, emit
import control
import time


app = Flask(__name__)
socketio = SocketIO(app, async_mode='threading')

@app.route("/")
def frontend():
    return render_template('index.html')

@app.route("/client")
def frontend_client():
    return render_template('client.html')

@socketio.on('timer_status')
def send_timer_status(status):
    emit('timer_status', status, broadcast=True)

@socketio.on('control')
def timer_control(d):
    if d == 'start':
        control.start_timer()
    if d == 'pause':
        control.pause_timer()

@socketio.on('connect')
def client_connected():
    emit('timer_status', control.get_status())
    emit('timer_updated', control.get_status()['timer_length'])
    control.run_time(time.time())

@socketio.on('set_timer')
def set_timer(d):
    control.set_timer(d)
    emit('timer_updated', control.get_status()['timer_length'], broadcast=True)

@socketio.on('reset_timer')
def reset_timer():
    control.reset_timer()

@socketio.on('blackout')
def blackout(data):
    emit('blackout', 'blackout', broadcast=True)

@socketio.on('time_updated')
def send_time(data):
    emit('time_updated', data, broadcast=True)