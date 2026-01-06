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
            width: int,
            height: int,
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

        self._title_color : ANSI = Color(Color.C_BG)
        self._reset_color : ANSI = Color(Color.C_RESET)
        self._width : int = width
        self._height : int = height
        self._screen : list[list[dict]] = []

        for _ in range(self._height):
            self._screen.append([])
            for _ in range(self._width):
                self._screen[-1].append({
                    "name" : "",
                    "action" : TUI.none,
                    "data" : None,
                    "color" : Color(Color.C_RESET)
                })


    def __str__(
            self
        ) -> str:
        """
            Return the string representation of the TUI.
        """

        from epitech_console.ANSI.color import Color

        string : str = ""
        for line in self._screen:
            for column in line:
                string += f"{column['color']}{column['name']}{Color(Color.C_RESET)}  "
            string = string[:-2] + "\n"

        return string[:-1]


    def add(
            self,
            x: int,
            y: int,
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

        self._screen[x][y]["name"] = name

        if action is not None:
            self._screen[x][y]["action"] = action

        if data is not None:
            self._screen[x][y]["data"] = data

        if color is not None:
            self._screen[x][y]["color"] = color


    def fill(
            self
        ) -> None:
        pass


    @staticmethod
    def none(
        ) -> None:
        """
            Nothing
        """
        pass
