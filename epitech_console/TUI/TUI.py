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


    def __init__(
            self,
            *args,
            **kwargs
        ) -> None:
        """
            Create a TUI (Terminal User Interface).
        """

        from epitech_console.ANSI.ansi import ANSI
        from epitech_console.ANSI.color import Color
        from epitech_console.System.console import Console

        self._title_color : ANSI = Color(Color.C_BG)
        self._reset_color : ANSI = Color(Color.C_RESET)
        self._width : int = Console.get_size()[0] - 1
        self._height : int = Console.get_size()[1]

        self._screen : list[list[Any]] = []


