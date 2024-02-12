import threading
import socketio
import time

sio = None

def connect_socket():
    global sio
    sio = socketio.SimpleClient()
    sio.connect("http://localhost:8000")
    

timer_length = 0
current_time = 0
fraction = 0

running = False
timer_thread = None

def seconds_to_string(s):
    mins, secs = divmod(s, 60) 
    timerstring = '{:02d}:{:02d}'.format(mins, secs) 
    return str(timerstring)


def get_status():
    return {
        "current_time": seconds_to_string(current_time),
        "running": running,
        "timer_length": timer_length / 60
        }

def emit_status():
    if sio == None:
        connect_socket()
    sio.emit('timer_status', get_status())

def set_timer(seconds):
    global timer_length, current_time, running
    timer_length = seconds
    running = False
    if timer_thread is not None:
        timer_thread.cancel()
    current_time = seconds
    #tk_display.update_screen(current_time)
    emit_status()
    

def start_timer():
    global running
    if not running:
        running = True
        emit_status()
        run_timer(time.time())


def pause_timer():
    global running, current_time
    if running:
        timer_thread.cancel()
        running = False
    else:
        current_time = timer_length
    emit_status()
    #tk_display.update_screen(current_time)

def run_timer(previous_time_projection):
    global current_time, timer_thread, sio, running, fraction
    diff = 1 - (time.time() - previous_time_projection)
    timer_thread = threading.Timer(diff, run_timer, args=(time.time() + diff,))
    timer_thread.start()
    if current_time == 0:
        running = False
    #tk_display.update_screen(current_time)
    emit_status()
    if current_time > 0 and running:
        current_time -= 1
    else:
        timer_thread.cancel()
        