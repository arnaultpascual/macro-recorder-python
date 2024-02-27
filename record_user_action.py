import time
from pynput import mouse, keyboard
from pynput.mouse import Button as MouseButton
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Controller as MouseController

# Global list to store actions
actions = []
start_time = time.time()

def on_click(x, y, button, pressed):
    action_type = 'mouse_click' if pressed else 'mouse_release'
    actions.append((action_type, str(x), str(y), str(button), str(time.time() - start_time)))

def on_scroll(x, y, dx, dy):
    actions.append(('mouse_scroll', str(x), str(y), str(dx), str(dy), str(time.time() - start_time)))

def on_press(key):
    if key == Key.esc:
        # Stop listener
        return False
    else:
        actions.append(('key_press', str(key), str(time.time() - start_time)))

def on_release(key):
    actions.append(('key_release', str(key), str(time.time() - start_time)))

def start_listening():
    # Start listening to mouse
    with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as listener_mouse:
        # Start listening to keyboard
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener_keyboard:
            print("Start recording... Press ESC to stop.")
            listener_keyboard.join()

    # Saving actions to a file
    with open('recorded_actions.txt', 'w') as file:
        for action in actions:
            file.write(','.join(map(str, action)) + '\n')

    print("Recording stopped and saved.")

start_listening()
