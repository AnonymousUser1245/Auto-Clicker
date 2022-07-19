import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

keybind = str(input(
    "Choose a keybind then press enter (must be 1 key excluding enter, shift, caps lock): "))
print('''

# SPEEDS
# 1 = 64cps
# 2 = 128cps
# 3 = 192cps
# 4 = 258cps - maybe unstable
# 5 = 327cps - maybe unstable
# 6 = 390cps - unstable
# 7 = 440cps - unstable
# 8 = 536cps - very unstable
# 9 = 560cps - very unstable
# 10 = 606cps - 99% unstable (can crash computer)

''')
speed = int(input("Speed (1 - 10): "))

TOGGLE_KEY = KeyCode(char=keybind)

clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, speed)
        time.sleep(0.001)


def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
