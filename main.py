from pynput.mouse import Listener, Button
from pynput import keyboard
import pydirectinput

# Global variable to track the listener state
listening = False
listener = None


# Function to hold down button
def hold_btn(btnName):
    pydirectinput.press(btnName)

# Function to release the button
def release_btn(btnName):
    pydirectinput.keyUp(btnName)

def press_btn(btnName):
    pydirectinput.press(btnName)

# Callback when a mouse button is pressed or released
def on_click(x, y, button, pressed):
    if button == Button.right:
        if pressed:
            hold_btn('x')
        else:
            release_btn('x')

    elif button == Button.left:
        if pressed:
            press_btn('c')

# Callback when a keyboard key is pressed
def on_key_press(key):
    global listening, listener

    try:
        if key == keyboard.Key.f1:  # Change this to your desired key combination
            if not listening:
                print("Key combination detected. Starting the listener.")
                listener = Listener(on_click=on_click)
                listener.start()
                listening = True
            else:
                print("Key combination detected. Stopping the listener.")
                listener.stop()
                listening = False
        if key == keyboard.Key.caps_lock:
            return False
        
    except AttributeError:
        pass

def main():
    print("Press F1 to start or stop the listener.")
    print("Press Caps Lock to stop the script.")

    with keyboard.Listener(on_press=on_key_press) as key_listener:
        key_listener.join()

if __name__ == "__main__":
    main()