#############################
###                       ###
###    Epitech Console    ###
###     ----TUI.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any


from epitech_console.System.setting import Setting


Setting.update()


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Text.Format: imported")


class TUI:
    """
        TUI class.

        TUI tool.
    """


    from collections.abc import Callable
    from epitech_console.System.action import Action, Actions
    from epitech_console.ANSI.color import Color


    def __init__(
            self,
            height: int,
            width: int,
            **kwargs
        ) -> None:
        """
            Create a TUI (Terminal User Interface).

            Parameters:
                width (int): width of the TUI.
                height (int): height of the TUI.
        """

        from epitech_console.ANSI.ansi import ANSI
        from epitech_console.ANSI.color import Color
        from epitech_console.System.console import Console

        self._screen : list[list[dict]] = []
        self.separator : str = "=="
        self._width : int = width
        self._height : int = height
        self.title : str = ">>>  TUI  <<<"
        self.title_color : ANSI = Color.rgb_bg(255, 255, 255) + Color.rgb_fg(50, 50, 50)
        self._element_length = ((len(Console)) // self._width) - len(self.separator)
        self._element_base : str = (' ' * self._element_length)
        self.element_color : ANSI = Color.rgb_bg(50, 50, 50) + Color.rgb_fg(255, 255, 255)
        self._total_length : int = (self._element_length * self._width) + (len(self.separator) * (self._width - 1))
        self.selection_color : ANSI = Color.rgb_bg(150, 150, 150) + Color.rgb_fg(50, 50, 50)
        self._running : bool = False
        self.selection : tuple = (0, 0)
        self._base_element : dict = {
            "name" : self._element_base,
            "action" : TUI._none,
            "data" : None,
            "color" : self.element_color
        }

        if "title" in kwargs and type(kwargs["title"]) == str:
            self.title = kwargs["title"]

        if "title_color" in kwargs and type(kwargs["title_color"]) == ANSI:
            self.title_color = kwargs["title_color"]

        if "element_color" in kwargs and type(kwargs["element_color"]) == ANSI:
            self.element_color = kwargs["element_color"]

        if "selection_color" in kwargs and type(kwargs["selection_color"]) == ANSI:
            self.selection_color = kwargs["selection_color"]

        if "separator" in kwargs and type(kwargs["separator"]) == str:
            self.separator = kwargs["separator"]

        for _ in range(self._height):
            self._screen.append([])

            for _ in range(self._width):
                self._screen[-1].append(self._base_element.copy())


    def __str__(
            self
        ) -> str:
        """
            Return the string representation of the TUI.
        """

        from epitech_console.ANSI.color import Color
        from epitech_console.System.console import Console

        string : str = f"{self.title_color + Color(Color.C_BOLD)}{" " * ((self._total_length - len(self.title)) // 2)}{self.title}{" " * ((self._total_length - len(self.title)) // 2)}{" " * (len(Console) - (self._total_length - 1))}{Color(Color.C_RESET)}\n"

        for line in range(self._height):
            string += f"{self.title_color} {Color(Color.C_RESET)}{self.element_color}"

            for column in range(self._width):
                string += f"{Color(Color.C_RESET)}{self.selection_color if line == self.selection[0] and column == self.selection[1] else self._screen[line][column]['color']}{self._screen[line][column]['name']}{Color(Color.C_RESET)}{self.element_color}{self.separator}"

            string = string[:-2] + f"{Color(Color.C_RESET)}{self.title_color} "
            string += (" " * (len(Console) - (self._total_length + 2))) + str(Color(Color.C_RESET)) + "\n"

        string += f"{self.title_color + Color(Color.C_BOLD)}{" " * len(Console)}{Color(Color.C_RESET)}\n"

        return string[:-1]


    def add(
            self,
            y: int,
            x: int,
            name: str,
            *,
            action: Action | Actions | Callable | None = None,
            data: Any | None = None,
            color: Color | None = None
        ) -> None:
        """
            Add an element to interact with.

            Parameters:
                x (int): x position of the element.
                y (int): y position of the element.
                name (str): name of the element to show.
                action (Action | Actions | Callable | None, optional): action(s) to perform when the element is interacted with.
                data (Any | None, optional): data linked to the element (hidden behind the scene).
                color (Color | None, optional): color of the element.
        """

        y, x = y - 1, x - 1

        if len(name) > self._element_length:
            self._screen[y][x]["name"] = name[:self._element_length]

        else:
            empty_len = (self._element_length - len(name))
            self._screen[y][x]["name"] = (" " * (empty_len // 2)) + name + (" " * (empty_len - (empty_len // 2)))

        if action is not None:
            self._screen[y][x]["action"] = action

        if data is not None:
            self._screen[y][x]["data"] = data

        if color is not None:
            self._screen[y][x]["color"] = color


    def delete(
            self,
            y: int,
            x: int
        ) -> None :
        """
            Delete an element from the TUI.
        """

        y, x = y - 1, x - 1

        self._screen[y][x] = self._base_element.copy()


    def fill(
            self,
            filler: str = ""
        ) -> None:
        """
            Fill the TUI with string.
        """

        from epitech_console.ANSI.color import Color

        if len(filler) > self._element_length:
            filler = filler[:self._element_length]

        else:
            empty_len = (self._element_length - len(filler))
            filler = (" " * (empty_len // 2)) + filler + (" " * (empty_len - (empty_len // 2)))

        for line in range(self._height):
            for column in range(self._width):
                copy = self._base_element.copy()
                copy["name"] = filler
                self._screen[line][column] = copy


    def run(
            self
        ) -> None:
        """
            Start the TUI.
        """

        from epitech_console.System.console import Console
        from epitech_console.ANSI.cursor import Cursor
        from epitech_console.ANSI.line import Line

        self._running = True
        pressed_key : str

        Console.print(Cursor.hide(), end = "")

        while self._running:
            Console.print(Line.clear() + str(self), end = "")
            pressed_key = Console.get_key_press()

            if pressed_key == "q":
                self._running = False
            elif pressed_key == "\x1b[A":
                self.selection = (self.selection[0] - 1, self.selection[1])
            elif pressed_key == "\x1b[B":
                self.selection = (self.selection[0] + 1, self.selection[1])
            elif pressed_key == "\x1b[C":
                self.selection = (self.selection[0], self.selection[1] + 1)
            elif pressed_key == "\x1b[D":
                self.selection = (self.selection[0], self.selection[1] - 1)
            elif pressed_key == "\r":
                self._screen[self.selection[0]][self.selection[1]]["action"]()

            if self.selection[0] < 0:
                self.selection = (self.selection[0] + self._height, self.selection[1])
            elif self.selection[0] >= self._height:
                self.selection = (self.selection[0] - self._height, self.selection[1])

            if self.selection[1] < 0:
                self.selection = (self.selection[0], self.selection[1] + self._width)
            elif self.selection[1] >= self._width:
                self.selection = (self.selection[0], self.selection[1] - self._width)

        Console.print(Line.clear() + Cursor.show(), end = "")


    def exit(
            self
        ) -> None:
        """
            Stop the TUI.
        """

        self._running = False


    @staticmethod
    def _none(
        ) -> None:
        """
            Nothing
        """
        pass
