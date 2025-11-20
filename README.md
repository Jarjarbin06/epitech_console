## Epitech Student's project

![Project Logo](https://www.epitech.eu/wp-content/uploads/Epitech-Accueil.png "Epitech logo")



# epitech_console 👋

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Stars](https://img.shields.io/github/stars/Jarjarbin06/epitech_console?style=social)](https://github.com/Jarjarbin06/epitech_console)

## Description

The `epitech_console` is a friendly Python tool that helps you create cool stuff in your terminal! It's like giving your command-line interface a makeover with fun animations, colorful text, and neat formatting. If you want to make your terminal programs look more interesting and organized, this library is for you!

## Table of Contents

1.  [Description](#Description)
2.  [Features](#Features)
3.  [Tech Stack](#Tech-Stack)
4.  [Installation](#Installation)
5.  [Usage](#Usage)
6.  [Project Structure](#Project-Structure)
7.  [API Reference](#API-Reference)
8.  [License](#License)
9. [Important Links](#Important-Links)
10. [Footer](#Footer)

## Features

*   **Cool Text Effects**: Easily add colors, bold text, italics, underlines, and even strikethroughs to your terminal text.
*   **Animations**: Make your terminal come alive with simple animations. Great for loading screens or just adding some visual flair!
*   **Progress Bars**: Show the progress of long tasks with customizable progress bars.  Keep your users informed in a visually appealing way.
*   **Timers**: Use the built-in stopwatch to measure how long parts of your code take to run.
*   **Configuration**: Easily manage settings for your application.
*   **Error Handling**:  Clear and helpful error messages to make debugging easier.
*   **Cursor Control**:  Move the cursor around, hide it, or show it as needed.
*   **Line Control**:  Quickly clear lines or the entire screen.

*   **ANSI Escape Sequence Handling**: Provides classes for generating ANSI escape sequences to control text color, formatting, and cursor movement.
*   **Text Formatting**: Includes tools for applying styles like bold, italic, underline, and strikethrough to text.
*   **Animation**: Supports creating and displaying animations in the console.
*   **Progress Bars**: Offers progress bar functionality to visualize task completion.
*   **Stopwatch**: Includes a stopwatch class for measuring elapsed time.
*   **Configuration Management**: Provides a configuration system to handle settings and preferences.
*   **Error Handling**: Custom error class for more informative error messages.
*   **Cursor Manipulation**: Ability to move, show and hide the cursor.
*   **Line Manipulation**: Clear lines, clear screen functionality.

## Tech-Stack

*   **Language**: Python - Because who doesn't love Python?
*   **Frameworks**: Python -  It's all Python, all the way!

## Installation

Ready to get started? Here's how to install `epitech_console`:

1.  **First Things First**: Make sure you have Python 3.13 or newer installed on your computer. You can check your Python version by opening a terminal and typing `python --version`.

2.  **Install with `pip` (Easy Method)**:

    Open your terminal and run this command:

    ```bash
    pip install epitech_console
    ```

    This will automatically download and install the library from PyPI.

    **Alternative: Install from GitHub**:

    If you want the latest version directly from the source, you can install it using `git`:

    ```bash
    git clone git@github.com:Jarjarbin06/epitech_console.git
    cd epitech_console
    ./install-package
    ```

    This downloads the code, then the `install-package` script handles the installation.

    These commands installs the `epitech_console` package and its dependencies (None currently).

## Usage

Here are some simple examples to get you started with `epitech_console`:

### Basic Text Formatting

```python
from epitech_console import Text, ANSI

epitech_color = ANSI.Color.epitech_fg() + ANSI.Color.rgb_bg(0, 0 ,0)
reset = ANSI.Color.color(ANSI.Color.C_RESET)
my_text = epitech_color + Text.Text("hi").bold() + reset

print(my_text)
```

### Creating an Animation

```python
from epitech_console import Animation, System

my_animation = Animation.Animation(Animation.BasePack.P_FILL_R)
for i in range(5):
    System.Console.print(my_animation.render(delete=True), sleep=0.5)
    my_animation.update()
```

### Creating a custom Animation

```python
from epitech_console import Animation, System

my_animation = Animation.Animation(['Frame 1', 'Frame 2', 'Frame 3'])
for i in range(5):
    System.Console.print(my_animation.render(delete=True), sleep=0.5)
    my_animation.update()
```

### Using a Progress Bar

```python
from epitech_console.Animation import ProgressBar, Spinner
from epitech_console import System

spinner = Spinner.stick()
progress_bar = ProgressBar(length=20, percent_style="mix", spinner=spinner)
for i in range(101):
    progress_bar.update(percent=i, update_spinner=(i % 5 == 0))
    System.Console.print(progress_bar.render(delete=True), sleep=0.05)
```

### Utilizing the Stopwatch

```python
from epitech_console import System

stopwatch = System.StopWatch(start=True)
System.Time.sleep(2)
stopwatch.stop()
print(f"Elapsed time: {stopwatch.elapsed()}")
```

### Create a config.ini file

```python
from epitech_console.System import Config

path = "."
if Config.is_empty(path):
    Config.create(path, {
      "GENERALE" : {"theme": "dark", "language": "en"},
      "USER" : {"username": "guest", "email": "my_email@email.com"}
    })
```

This will check and create a `config.ini` file if it doesn't exist.

## Project-Structure

```
epitech_console/
├── Animation/
│   ├── __init__.py
│   ├── animation.py
│   ├── basepack.py
│   ├── progressbar.py
│   ├── spinner.py
│   └── style.py
├── ANSI/
│   ├── __init__.py
│   ├── ansi.py
│   ├── basepack.py
│   ├── color.py
│   ├── cursor.py
│   └── line.py
├── Error/
│   ├── __init__.py
│   └── error.py
├── System/
│   ├── __init__.py
│   ├── config.py
│   ├── console.py
│   ├── stopwatch.py
│   └── time.py
├── Text/
│   ├── __init__.py
│   ├── format.py
│   └── text.py
├── __init__.py
├── config.ini
├── install-package
├── LICENSE
└── pyproject.toml
```

## API-Reference

### Animation Module

*   **Animation**: Class for creating animations.
    *   `Animation(animation: list[str] | str = "")`: Constructor to create an animation.
    *   `update(auto_reset: bool = True)`: Advances the animation by one step.
    *   `render(delete: bool = False)`: Renders the current frame of the animation.
*   **ProgressBar**: Class for creating progress bars.
    *   `ProgressBar(length: int, animation: Animation | None = None, style: object = Style("#", "-", "<", ">", "|", "|"), percent_style: str = "bar", spinner: Animation | None = None, spinner_position: str = "a")`: Constructor to create a progress bar.
    *   `update(percent: int = 0, update_spinner: bool = True, auto_reset: bool = True)`: Updates the progress bar to a specified percentage.
    *   `render(color: object | tuple[object, object, object] = Color.color(Color.C_RESET), hide_spinner_at_end: bool = True, delete: bool = False)`: Renders the progress bar.
*   **Style**: Class for styling progress bars.
    *   `Style(on: str = "#", off: str = "-", arrow_left: str = "<", arrow_right: str = ">", border_left: str = "|", border_right: str = "|")`: Constructor to create a style.
*   **Spinner**: Class with pre-built spinner animations.
    *   `stick(style: object = Style("#", " ", "#", "#", "", ""))`: Creates a stick spinner.
    *   `plus(style: object = Style("#", " ", "#", "#", "", ""))`: Creates a plus spinner.
    *   `cross(style: object = Style("#", " ", "#", "#", "", ""))`: Creates a cross spinner.

### ANSI Module

*   **ANSI**: Class for creating ANSI escape sequences.
    *   `ANSI(sequence: str = "")`: Constructor to create an ANSI sequence.
    *   `ESC`: ANSI escape character.
*   **Color**: Class for ANSI color codes.
    *   Provides static methods for foreground (`color_fg`) and background (`color_bg`) colors.
    *   `rgb_fg(r: int, g: int, b: int)`: Returns ANSI sequence for a foreground RGB color.
    *   `rgb_bg(r: int, g: int, b: int)`: Returns ANSI sequence for a background RGB color.
*   **Cursor**: Class for cursor manipulation.
    *   `up(n: int = 1)`: Moves the cursor up `n` lines.
    *   `down(n: int = 1)`: Moves the cursor down `n` lines.
    *   `left(n: int = 1)`: Moves the cursor left `n` columns.
    *   `right(n: int = 1)`: Moves the cursor right `n` columns.
    *   `hide()`: Hides the cursor.
    *   `show()`: Shows the cursor.
*   **Line**: Class for line manipulation.
    *   `clear_line()`: Clears the current line.
    *   `clear_screen()`: Clears the entire screen.

### System Module

*   **StopWatch**: Class for measuring elapsed time.
    *   `StopWatch(start: bool = False)`: Constructor to create a stopwatch.
    *   `start()`: Starts the stopwatch.
    *   `stop()`: Stops the stopwatch.
    *   `elapsed()`: Returns the elapsed time.
*   **Time**: Class for time-related functions.
    *   `sleep(seconds: int | float)`: Pauses execution for a specified number of seconds.
*   **Config**: Class for configuration management.
    *   `is_empty(path: str) -> bool`: Checks if a config file is empty.
    *   `create(path: str, data: dict | None = None)`: Creates a new config file.
*   **Console**: Class for console output.
    *   `print(value: any = "", start: str = "", end: str = "\n", file: any = stdout, sleep: int | float | None = None)`: Prints to the console with optional start, end, file, and sleep parameters.

### Text Module

*   **Text**: Class for handling text.
    *   `Text(text: object | str = "")`: Constructor to create a text object.
    *   `clion_link(path: str, line: int | None = None)`: Creates a CLion link to a file and line number.

### Error Module

*   **Error**: Class for custom error handling.
    *   `Error(message: str = "an error occurred", error: str = "Error", link: tuple[str, int] | None = None)`: Constructor to create an error object.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://github.com/Jarjarbin06/epitech_console/blob/ad808d437817f8ea2cd44e4a33a38238a41f83c4/LICENSE) file for details.

## Important-Links

*   **Repository**: [https://github.com/Jarjarbin06/epitech_console](https://github.com/Jarjarbin06/epitech_console)

## Footer

*   Repository: [epitech_console](https://github.com/Jarjarbin06/epitech_console)
*   Author: Nathan Jarjarbin
*   Contact: nathan.amaraggi@epitech.eu

⭐️ Like the project? Give it a star!
🐛 Found a bug? Report it in the issues!


---
**<p align="center">Generated by [ReadmeCodeGen](https://www.readmecodegen.com/)</p>**