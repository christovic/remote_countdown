import tkinter as tk
import socketio
import json

with open("port.json") as f:
    port = json.load(f)['port']
global sio
sio = socketio.Client()
sio.connect(f"http://localhost:{port}")

@sio.on('timer_status')
def incoming_ws(data):
    update_screen(data['current_time'])

def setup_gui():
    global window
    global timelabel
    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.geometry("1920x1080")


    timelabel = tk.Label(
        text="00:00",
        font=("monospace", 400),
        fg="white",
        bg="black",
        width=window.winfo_screenwidth(),
        height=window.winfo_screenheight()
        )
    timelabel.pack()


def start_gui():        
    window.mainloop()

def update_screen(incoming, background_colour='black'):
    timelabel.config(text=incoming, background=background_colour)

def seconds_to_string(s):
    mins, secs = divmod(s, 60) 
    timerstring = '{:02d}:{:02d}'.format(mins, secs) 
    return str(timerstring)

setup_gui()
start_gui()
