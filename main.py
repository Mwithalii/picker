import threading
import time

from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

#key to activate and deactivate the autoclicker
TOGGLE_KEY = KeyCode(char='t')

#indicate whether clicking is activated or not
clicking = False

mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.001)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking
        print('clicking is {}'.format(clicking))

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()