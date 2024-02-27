import time
from pynput.mouse import Button as MouseButton, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from ast import literal_eval

def replay_actions(filename):
    mouse_controller = MouseController()
    keyboard_controller = KeyboardController()

    with open(filename, 'r') as file:
        previous_time = 0
        for line in file:
            parts = line.strip().split(',')
            action = parts[0]
            action_time = float(parts[-1])

            # Calculate the delay based on the recorded time
            delay = action_time - previous_time
            time.sleep(delay)
            previous_time = action_time

            if action in ['mouse_click', 'mouse_release']:
                x, y, button_name = parts[1:4]
                x, y = int(x), int(y)
                button = MouseButton.left if 'left' in button_name else MouseButton.right
                mouse_controller.position = (x, y)
                if action == 'mouse_click':
                    mouse_controller.press(button)
                else:
                    mouse_controller.release(button)
            elif action == 'mouse_scroll':
                dx, dy = literal_eval(parts[1]), literal_eval(parts[2])
                mouse_controller.scroll(dx, dy)
            elif action in ['key_press', 'key_release']:
                key_str = ','.join(parts[1:-1])  # Re-join the key parts in case it was split by commas
                try:
                    # Check if key_str corresponds to a special key
                    if key_str.startswith('Key.'):
                        key = getattr(Key, key_str[len('Key.'):])  # Extract and use special Key attribute
                    else:
                        # Directly use the character for regular keys
                        key = key_str.replace("'", "")  # Remove any single quotes from the key string
                        
                    print(f"Attempting to {action} key: {key}")  # Debugging output
                    if action == 'key_press':
                        keyboard_controller.press(key)
                    elif action == 'key_release':
                        keyboard_controller.release(key)
                except Exception as e:
                    print(f"Error handling key {key_str}: {e}")

if __name__ == "__main__":
    replay_actions('recorded_actions.txt')
