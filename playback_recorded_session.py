import time
from pynput.mouse import Button as MouseButton, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from ast import literal_eval

# Initialize controllers for mouse and keyboard actions
mouse_controller = MouseController()
keyboard_controller = KeyboardController()

# Simulates a mouse click
def mouse_click(parts):
    x, y, button_name = int(parts[1]), int(parts[2]), parts[3]
    button = MouseButton.left if 'left' in button_name else MouseButton.right
    mouse_controller.position = (x, y)
    mouse_controller.press(button)

# Simulates releasing a mouse button
def mouse_release(parts):
    x, y, button_name = int(parts[1]), int(parts[2]), parts[3]
    button = MouseButton.left if 'left' in button_name else MouseButton.right
    mouse_controller.position = (x, y)
    mouse_controller.release(button)

# Handles mouse scroll actions
def mouse_scroll(parts):
    dx, dy = literal_eval(parts[1]), literal_eval(parts[2])
    mouse_controller.scroll(dx, dy)

# Initiates a key press action
def key_press(parts):
    handle_key_action(parts, "press")

# Initiates a key release action
def key_release(parts):
    handle_key_action(parts, "release")

# Helper to manage key press/release, supporting special keys
def handle_key_action(parts, action_type):
    key_str = ','.join(parts[1:-1])
    try:
        key = getattr(Key, key_str.split('.')[-1]) if key_str.startswith('Key.') else key_str.strip("'")
        action = keyboard_controller.press if action_type == "press" else keyboard_controller.release
        action(key)
    except AttributeError:
        print(f"Error with key: {key_str}. Key not found.")

# Maps supported actions to their handlers
action_functions = {
    'mouse_click': mouse_click,
    'mouse_release': mouse_release,
    'mouse_scroll': mouse_scroll,
    'key_press': key_press,
    'key_release': key_release
}

# Replays actions from a specified file, managing time delays and action dispatch
def replay_actions(filename):
    try:
        with open(filename, 'r') as file:
            previous_time = 0
            for line in file:
                parts = line.strip().split(',')
                action, action_time = parts[0], float(parts[-1])
                
                time.sleep(action_time - previous_time)  # Delay execution to match recorded timing
                previous_time = action_time

                if action in action_functions:
                    action_functions[action](parts)  # Dispatch to appropriate handler
                else:
                    print(f"Unsupported action: {action}")

    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    replay_actions('recorded_actions.txt')
