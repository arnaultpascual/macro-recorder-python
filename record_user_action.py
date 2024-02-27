import time
from pynput import mouse, keyboard

# Global list to store user actions and the start time for the recording
actions = []
start_time = time.time()

def on_click(x, y, button, pressed):
    """
    Handles mouse click and release events.
    
    Parameters:
    - x, y: The position of the mouse cursor.
    - button: Which mouse button was pressed or released.
    - pressed: True if the button was pressed, False if released.
    """
    action_type = 'mouse_click' if pressed else 'mouse_release'
    actions.append((action_type, x, y, button, time.time() - start_time))

def on_scroll(x, y, dx, dy):
    """
    Handles mouse scroll events.
    
    Parameters:
    - x, y: The position of the mouse cursor.
    - dx, dy: The scroll distance in x (horizontal) and y (vertical) directions.
    """
    actions.append(('mouse_scroll', x, y, dx, dy, time.time() - start_time))

def on_press(key):
    """
    Handles key press events.
    
    Parameters:
    - key: The key that was pressed.
    """
    if key == keyboard.Key.esc:
        # Stop listener if escape key is pressed
        return False
    else:
        actions.append(('key_press', key, time.time() - start_time))

def on_release(key):
    """
    Handles key release events.
    
    Parameters:
    - key: The key that was released.
    """
    actions.append(('key_release', key, time.time() - start_time))

def start_listening():
    """
    Starts listeners for both mouse and keyboard actions.
    Records actions until the escape key is pressed.
    """
    try:
        with mouse.Listener(on_click=on_click, on_scroll=on_scroll) as listener_mouse, \
             keyboard.Listener(on_press=on_press, on_release=on_release) as listener_keyboard:
            print("Start recording... Press ESC to stop.")
            listener_keyboard.join()  # Wait until keyboard listener is stopped

        # Saving actions to a file safely
        with open('recorded_actions.txt', 'w') as file:
            for action in actions:
                file.write(','.join(map(str, action)) + '\n')

        print("Recording stopped and saved.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    start_listening()
