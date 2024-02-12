from flask import Flask
from flask import request, render_template
from flask_socketio import SocketIO, emit
import threading
import subprocess
import control

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

@socketio.on('set_timer')
def set_timer(d):
    control.set_timer(d)
    emit('timer_updated', control.get_status()['timer_length'], broadcast=True)

def start_flask():
    app.run(host="127.0.0.1")
if __name__ == "__main__":
    threading.Thread(target=app.run, kwargs={'host':"0.0.0.0", 'port':8080}).start()
    #tk_display.setup_gui()
    #start_gunicorn_thread()
    #threading.Thread(target=tk_display.start_gui).start()
    #tk_display.start_gui()
