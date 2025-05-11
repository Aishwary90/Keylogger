from pynput.keyboard import Listener, Key

def on_press(key):
    print(f"You pressed: {key}")
    if key == Key.esc:
        print("Stopping... Pressed Esc to exit.")
        return False

print("Starting keyboard listener. Press Esc to stop.")
with Listener(on_press=on_press) as listener:
    listener.join()

# This code sets up a keyboard listener that prints the key pressed to the console.
# It stops listening when the Esc key is pressed.dsdsdccc