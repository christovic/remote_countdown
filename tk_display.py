import tkinter as tk
import socketio

global sio
sio = socketio.Client()
sio.connect("http://localhost:8000")

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
# def start_countdown(t):
#     global current_time
#     global after_id
#     current_time = t
#     if t > -1 and running:
#         send_timer_status({'running': True, 'remaining': seconds_to_string(t)})
#         timelabel.config(text=seconds_to_string(t))
#         after_id = window.after(1000, start_countdown, t-1) 

# def start():
#     global running
#     running = True
#     start_countdown(timer)

# def pause():
#     global running, timer, current_time
#     running = False
#     window.after_cancel(after_id)
#     timer = current_time

# def set_timer(t):
#     global timer
#     timer = t
#     global timelabel
#     timelabel.config(text=seconds_to_string(t))
#     if running:
#         window.after_cancel(after_id)
#         start_countdown(timer)
