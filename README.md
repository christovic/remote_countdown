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
5. Visit the IP of the computer you're running this on in the browser with port :8000. For example, if your computer IP address is 192.168.1.100, enter http://192.168.1.100:8000 in the browser.

The controller is on `/` and the client is on `/client`. You can click on the timer in the controller to access the client.

If you wish to have a local display on the server show the countdown timer, please pass the `--local-screen` parameter.

If you wish to run this on another port, please specify `--port` when running.

## Keyboard mappings

If you'd like to use a keyboard to control the interface, the following keys are bound:

- Enter:

When minutes have been typed in, this will update all screens to the new timer, but not start.

- Spacebar:

When minutes have been typed in, this will update all screens to the new timer and **immediately** start the timer.

When minutes is empty and the timer is running, it will pause the timer.

When minutes is empty and the timer is not running, it will resume the timer.

- r

When pressed, r will reset the the timer to the original timer value

- b 

When pressed, b will set the text on all timers to "", or in other words, black out the timer.