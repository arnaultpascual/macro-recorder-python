
# User Action Recorder and Playback

This project consists of two Python scripts that work together to record user actions, including mouse movements, clicks, scrolls, and keyboard presses, and then play them back as recorded. This tool can be useful for automating repetitive tasks, testing, or demonstrating software functionalities.

## Overview

- **record_user_action.py**: Records user's mouse and keyboard actions and saves them to a file (`recorded_actions.txt`). The recording stops when the ESC key is pressed.
- **playback_recorded_session.py**: Reads the actions recorded in `recorded_actions.txt` and replays them, simulating the user's original actions.

## Installation

To use these scripts, you need Python installed on your system along with the `pynput` library, which is used for monitoring and controlling the keyboard and mouse.

### Requirements

- Python 3.x
- pynput

### Installing pynput

You can install `pynput` using pip:

```bash
pip install pynput
```

## Usage

### Recording User Actions

1. Run `record_user_action.py` to start recording your actions.
   
   ```bash
   python record_user_action.py
   ```

2. Perform the actions you want to record. The script will capture mouse clicks, scrolls, and keyboard presses.
3. Press the ESC key to stop recording. The actions will be saved to `recorded_actions.txt`.

### Playing Back Recorded Actions

1. Ensure `recorded_actions.txt` is in the same directory as `playback_recorded_session.py`.
2. Run `playback_recorded_session.py` to start the playback of the recorded session.

   ```bash
   python playback_recorded_session.py
   ```

The script will replay the actions as they were recorded, including the timing between actions.

## Contributions

Contributions are welcome! If you have suggestions for improvements or bug fixes, please feel free to fork the repository and submit a pull request.

## License

This project is open-source and available under the MIT License.
