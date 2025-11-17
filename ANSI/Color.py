#############################
###                       ###
###      Console v2.0     ###
###    ----Color.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

from builtins import object, any

class Color:
    """
        Color class.

        ANSI coloring system.

        Attributes:
            BASE (str): Base color.
            BOLD (str): Bold color.
            DARK_BASE (str): Dark base color.
            ITALIC (str): Italic color.
            UNDERLINE (str): Underline color.
            FLASH_1 (str): Flash color.
            FLASH_2 (str): Flash color.
            HIGHLIGHT (str): Highlight color.
            HIDDEN (str): Hidden color.
            CROSSED (str): Crossed color.
            DARK_GREY (str): Dark grey color.
            DARK_RED (str): Dark red color.
            DARK_GREEN (str): Dark green color.
            DARK_YELLOW (str): Dark yellow color.
            DARK_BLUE (str): Dark blue color.
            DARK_LAVANDA (str): Dark lavanda color.
            DARK_CYAN (str): Dark cyan color.
            DARK_WHITE (str): Dark white color.
            HIGHLIGHT_DARK_GREY (str): Highlight dark grey color.
            HIGHLIGHT_DARK_RED (str): Highlight dark red color.
            HIGHLIGHT_DARK_GREEN (str): Highlight dark green color.
            HIGHLIGHT_DARK_YELLOW (str): Highlight dark yellow color.
            HIGHLIGHT_DARK_BLUE (str): Highlight dark blue color.
            HIGHLIGHT_DARK_LAVANDA (str): Highlight dark lavanda color.
            HIGHLIGHT_DARK_CYAN (str): Highlight dark cyan color.
            HIGHLIGHT_DARK_WHITE (str): Highlight dark white color.
            GREY (str): Grey color.
            RED (str): Red color.
            GREEN (str): Green color.
            YELLOW (str): Yellow color.
            BLUE (str): Blue color.
            LAVANDA (str): Lavanda color.
            CYAN (str): Cyan color.
            WHITE (str): White color.
            HIGHLIGHT_GREY (str): Highlight grey color.
            HIGHLIGHT_RED (str): Highlight red color.
            HIGHLIGHT_GREEN (str): Highlight green color.
            HIGHLIGHT_YELLOW (str): Highlight yellow color.
            HIGHLIGHT_BLUE (str): Highlight blue color.
            HIGHLIGHT_LAVANDA (str): Highlight lavanda color.
            HIGHLIGHT_CYAN (str): Highlight cyan color.
            HIGHLIGHT_WHITE (str): Highlight white color.
    """

    BASE : str = "\033[0m"
    BOLD : str = "\033[1m"
    DARK_BASE : str = "\033[2m"
    ITALIC : str = "\033[3m"
    UNDERLINE : str = "\033[4m"
    FLASH_1 : str = "\033[5m"
    FLASH_2 : str = "\033[6m"
    HIGHLIGHT : str = "\033[7m"
    HIDDEN : str = "\033[8m"
    CROSSED : str = "\033[9m"
    DARK_GREY : str = "\033[30m"
    DARK_RED : str = "\033[31m"
    DARK_GREEN : str = "\033[32m"
    DARK_YELLOW : str = "\033[33m"
    DARK_BLUE : str = "\033[34m"
    DARK_LAVANDA : str = "\033[35m"
    DARK_CYAN : str = "\033[36m"
    DARK_WHITE : str = "\033[37m"
    HIGHLIGHT_DARK_GREY : str = "\033[40m"
    HIGHLIGHT_DARK_RED : str = "\033[41m"
    HIGHLIGHT_DARK_GREEN : str = "\033[42m"
    HIGHLIGHT_DARK_YELLOW : str = "\033[43m"
    HIGHLIGHT_DARK_BLUE : str = "\033[44m"
    HIGHLIGHT_DARK_LAVANDA : str = "\033[45m"
    HIGHLIGHT_DARK_CYAN : str = "\033[46m"
    HIGHLIGHT_DARK_WHITE : str = "\033[47m"
    GREY : str = "\033[90m"
    RED : str = "\033[91m"
    GREEN : str = "\033[92m"
    YELLOW : str = "\033[93m"
    BLUE : str = "\033[94m"
    LAVANDA : str = "\033[95m"
    CYAN : str = "\033[96m"
    WHITE : str = "\033[97m"
    HIGHLIGHT_GREY : str = "\033[100m"
    HIGHLIGHT_RED : str = "\033[101m"
    HIGHLIGHT_GREEN : str = "\033[102m"
    HIGHLIGHT_YELLOW : str = "\033[103m"
    HIGHLIGHT_BLUE : str = "\033[104m"
    HIGHLIGHT_LAVANDA : str = "\033[105m"
    HIGHLIGHT_CYAN : str = "\033[106m"
    HIGHLIGHT_WHITE : str = "\033[107m"

    @staticmethod
    def color_fg(
            color : int
        ) -> object:
        """
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import (Color.py)')

        return ANSI(f"{ANSI.ESC}38;5;{color}m")

    @staticmethod
    def color_bg(
            color : int
        ) -> object:
        """
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import (Color.py)')

        return ANSI(f"{ANSI.ESC}48;5;{color}m")

    @staticmethod
    def rgb_fg(
            r : int,
            g : int,
            b : int
        ) -> object:
        """
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import (Color.py)')

        return ANSI(f"{ANSI.ESC}38;5;{r};{g};{b}m")

    @staticmethod
    def rgb_bg(
            r : int,
            g : int,
            b : int
        ) -> object:
        """
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import (Color.py)')

        return ANSI(f"{ANSI.ESC}48;5;{r};{g};{b}m")
