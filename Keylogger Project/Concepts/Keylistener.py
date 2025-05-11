from pynput.keyboard import Listener, Key

def on_press(key):
        with open("key_log.txt", 'a') as log_file:
            log_file.write(f"{key}\n")
        if key == Key.esc:
            print("Stopping... the keyboard listener.")
            return False

with Listener(on_press=on_press) as listener:
        print("Starting keyboard listener. Press Esc to stop.")
        listener.join()
# This code sets up a keyboard listener that logs the key pressed to a file named "Key_log.txt".