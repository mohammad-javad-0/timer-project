```markdown
# Timer

This project is a simple timer built using the `Tkinter` library in Python. It allows you to set a countdown timer and display the current time. The timer can be useful for managing tasks or setting reminders.

## Features

- **Clock Display:** Shows the current time in 12-hour format.
- **Set Timer:** Allows you to set a timer for various intervals (5 minutes, 15 minutes, 20 minutes, 30 minutes, 45 minutes, and 60 minutes).
- **Sound Alert:** Plays a sound notification when the timer ends.
- **Reset Timer:** Ability to reset the timer at any time.

## Installation and Setup

To run this project, you need to install the following libraries:

```bash
pip install tkinter
pip install playsound
```

After installing the libraries, simply run the code to open the timer.

## Usage

1. **Set Timer:** Click on one of the buttons corresponding to the desired time intervals to set the timer.
2. **Start Timer:** After setting the time, click the "START" button to start the timer.
3. **Reset Timer:** You can reset the timer at any time by clicking the "RESET" button.

## Related Files

- `main.py`: The main file containing the timer code.
- `music/mixkit-clock-bells-hour-signal-1069.wav`: The sound file that plays when the timer finishes.
- `image/*.png`: The images for the timer buttons.

## Notes

- If invalid values are entered for hours, minutes, or seconds, an error message will prompt you to correct it.
- Ensure that the sound and image files are in the specified paths for the project to run correctly.

## Contributing

If you wish to improve or add new features, you can fork the project and make your changes. After making the changes, submit a pull request.
