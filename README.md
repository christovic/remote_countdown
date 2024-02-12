# Remote Countdown

Remote Countdown is a Python web application for running a timer with a remote interface.

## Installation & Usage

1. Install Python
2. Clone this repository and cd/chdir into it
3. Install requirements:
```bash
pip3 install -r requirements.txt
```
4. Run:
```bash
python3 start.py
```
5. Visit the IP of the computer you're running this on in the browser with port :8000.

The controller is on `/` and the client is on `/client`

If you wish to have a local display on the server show the countdown timer, please pass the --local-screen parameter.

If you wish to run this on another port, please specify --port when running.