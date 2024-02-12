import subprocess
import json
import threading
import argparse

parser = argparse.ArgumentParser(
    prog='Remote Countdown Server',
    description='Runs a web server on the port you specify',
)

parser.add_argument('--port', action='store', default="8000")
parser.add_argument('--bind-address', action='store', default="0.0.0.0")
parser.add_argument('--local-screen', action='store_true')
args = parser.parse_args()
print(args.port, args.bind_address)
with open("port.json", "w") as f:
    json.dump({'port': args.port}, f)


def start_gunicorn():
    subprocess.run(f"gunicorn main:app --worker-class eventlet -w 1 -b {args.bind_address}:{args.port}".split(" "))

threading.Thread(target=start_gunicorn).start()
if args.local_screen:
    subprocess.run("python3 tk_display.py".split(" "))
