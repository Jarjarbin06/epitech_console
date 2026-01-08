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
    from epitech_console.System.console import Console
    from epitech_console.ANSI.color import Color
    from epitech_console.ANSI.ansi import ANSI


    def __init__(
            self,
            height: int,
            width: int,
            *,
            size: int = len(Console),
            separator: str = "==",
            title: str = ">>>  TUI  <<<",
            title_color: ANSI = Color.rgb_bg(255, 255, 255) + Color.rgb_fg(50, 50, 50),
            element_color: ANSI = Color.rgb_bg(50, 50, 50) + Color.rgb_fg(255, 255, 255),
            selection_color: ANSI = Color.rgb_bg(150, 150, 150) + Color.rgb_fg(50, 50, 50),
            selection: bool = True,
            limit: tuple[int, int, int, int] | None = None
        ) -> None:
        """
            Create a TUI (Terminal User Interface).

            Parameters:
                width (int): width of the TUI.
                height (int): height of the TUI.
                size (int): size of the TUI.
                title (str, optional): title.
                title_color (ANSI, optional): color of the title.
                element_color (ANSI, optional): color of the element.
                selection_color (ANSI, optional): color of the selection.
                separator (str, optional): separator between the elements (recommended to have an even length).
                limit (tuple[int, int, int, int] | None, optional): limit the selection zone (y1, x1, y2, x2).
                selection (bool, optional): enable/disable selection.
        """

        from epitech_console.ANSI.ansi import ANSI

        self.size : int = size
        self._screen : list[list[dict]] = []
        self.separator : str = separator
        self._width : int = width
        self._height : int = height
        self.title : str = title
        self.title_color : ANSI = title_color
        self._element_length = (self.size // self._width) - len(self.separator)
        self._element_base : str = (' ' * self._element_length)
        self.element_color : ANSI = element_color
        self._total_length : int = 0
        self.selection_color : ANSI = selection_color
        self._running : bool = False
        self.limit : tuple[int, int, int, int] = (0, 0, self._height, self._width)
        self.selected : tuple[int, int] = (self.limit[0], self.limit[1])
        self.selection : bool = selection
        self._base_element : dict = {
            "name" : self._element_base,
            "action" : TUI._none,
            "data" : None,
            "color" : self.element_color
        }

        if limit is not None:
            self.limit = (limit[0] - 1, limit[1] - 1, limit[2], limit[3])
            self.selected: tuple[int, int] = (self.limit[0], self.limit[1])

        self._total_length = (self._element_length * self._width) + (len(self.separator) * (self._width - 1))

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

        string : str = f"{self.title_color + Color(Color.C_BOLD)}{" " * ((self._total_length - len(self.title)) // 2)}{self.title}{" " * ((self._total_length - len(self.title)) // 2)}{" " * (self.size - (self._total_length - 1))}{Color(Color.C_RESET)}\n"

        for line in range(self._height):
            string += f"{self.title_color} {Color(Color.C_RESET)}{self.element_color}"

            for column in range(self._width):
                string += f"{Color(Color.C_RESET)}{self.selection_color if (line == self.selected[0] and column == self.selected[1]) and self.selection else self._screen[line][column]['color']}{self._screen[line][column]['name']}{Color(Color.C_RESET)}{self.element_color}{self.separator}"

            string = string[:-2] + f"{Color(Color.C_RESET)}{self.title_color} "
            string += (" " * (self.size - (self._total_length + 2))) + str(Color(Color.C_RESET)) + "\n"

        string += f"{self.title_color + Color(Color.C_BOLD)}{" " * self.size}{Color(Color.C_RESET)}\n"

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

        Console.print(Line.clear(), end = "")

        while self._running:
            Console.print(Cursor.hide() + Cursor.top() + str(self), end = "")
            pressed_key = Console.get_key_press()

            if pressed_key == "q":
                self._running = False
            elif pressed_key in ["\x1b[A"]:
                self.selected = (self.selected[0] - 1, self.selected[1])
            elif pressed_key in ["\x1b[B"]:
                self.selected = (self.selected[0] + 1, self.selected[1])
            elif pressed_key in ["\x1b[C"]:
                self.selected = (self.selected[0], self.selected[1] + 1)
            elif pressed_key in ["\x1b[D"]:
                self.selected = (self.selected[0], self.selected[1] - 1)
            elif pressed_key in ["\r", " "]:
                self._screen[self.selected[0]][self.selected[1]]["action"]()

            if self.selected[0] < self.limit[0]:
                self.selected = (self.selected[0] + (self.limit[2] - self.limit[0]), self.selected[1])
            elif self.selected[0] >= self.limit[2]:
                self.selected = (self.selected[0] - (self.limit[2] - self.limit[0]), self.selected[1])

            if self.selected[1] < self.limit[1]:
                self.selected = (self.selected[0], self.selected[1] + (self.limit[3] - self.limit[1]))
            elif self.selected[1] >= self.limit[3]:
                self.selected = (self.selected[0], self.selected[1] - (self.limit[3] - self.limit[1]))

        Console.print(Line.clear() + Cursor.show(), end = "")


    def exit(
            self
        ) -> None:
        """
            Stop the TUI.
        """

        self._running = False


    def move(
            self,
            y: int,
            x: int
        ) -> None:
        """
            Move the selection in the TUI.

            Parameters:
                y (int): y position of the element.
                x (int): x position of the element.

            (if y is set to -1, it's position will not change)
            (if x is set to -1, it's position will not change)
        """

        assert self.limit[0] <= y <= self.limit[2] or y == -1
        assert self.limit[1] <= x <= self.limit[3] or x == -1

        self.selected = (y - 1 if y != -1 else self.selected[0], x - 1 if x != -1 else self.selected[1])


    @staticmethod
    def _none(
        ) -> None:
        """
            Nothing
        """
        pass
