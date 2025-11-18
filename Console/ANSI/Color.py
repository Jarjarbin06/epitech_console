#############################
###                       ###
###      Console v2.0     ###
###    ----Color.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


class Color:
    """
        Color class.

        ANSI coloring system.

        Attributes:
            C_RESET (str): Base color.
            C_BOLD (str): Bold color.
            C_DARK_BASE (str): Dark base color.
            C_ITALIC (str): Italic color.
            C_UNDERLINE (str): Underline color.
            C_FLASH_1 (str): Flash color.
            C_FLASH_2 (str): Flash color.
            C_HIGHLIGHT (str): Highlight color.
            C_HIDDEN (str): Hidden color.
            C_CROSSED (str): Crossed color.
            C_DARK_GREY (str): Dark grey color.
            C_DARK_RED (str): Dark red color.
            C_DARK_GREEN (str): Dark green color.
            C_DARK_YELLOW (str): Dark yellow color.
            C_DARK_BLUE (str): Dark blue color.
            C_DARK_LAVANDA (str): Dark lavanda color.
            C_DARK_CYAN (str): Dark cyan color.
            C_DARK_WHITE (str): Dark white color.
            C_HIGHLIGHT_DARK_GREY (str): Highlight dark grey color.
            C_HIGHLIGHT_DARK_RED (str): Highlight dark red color.
            C_HIGHLIGHT_DARK_GREEN (str): Highlight dark green color.
            C_HIGHLIGHT_DARK_YELLOW (str): Highlight dark yellow color.
            C_HIGHLIGHT_DARK_BLUE (str): Highlight dark blue color.
            C_HIGHLIGHT_DARK_LAVANDA (str): Highlight dark lavanda color.
            C_HIGHLIGHT_DARK_CYAN (str): Highlight dark cyan color.
            C_HIGHLIGHT_DARK_WHITE (str): Highlight dark white color.
            C_GREY (str): Grey color.
            C_RED (str): Red color.
            C_GREEN (str): Green color.
            C_YELLOW (str): Yellow color.
            C_BLUE (str): Blue color.
            C_LAVANDA (str): Lavanda color.
            C_CYAN (str): Cyan color.
            C_WHITE (str): White color.
            C_HIGHLIGHT_GREY (str): Highlight grey color.
            C_HIGHLIGHT_RED (str): Highlight red color.
            C_HIGHLIGHT_GREEN (str): Highlight green color.
            C_HIGHLIGHT_YELLOW (str): Highlight yellow color.
            C_HIGHLIGHT_BLUE (str): Highlight blue color.
            C_HIGHLIGHT_LAVANDA (str): Highlight lavanda color.
            C_HIGHLIGHT_CYAN (str): Highlight cyan color.
            C_HIGHLIGHT_WHITE (str): Highlight white color.
    """

    try:
        from Console.ANSI import ANSI
    except Exception:
        raise ImportError('ANSI failed to import in Color.py')


    C_RESET : str = "\033[0m"
    C_BOLD : str = "\033[1m"
    C_DARK_BASE : str = "\033[2m"
    C_ITALIC : str = "\033[3m"
    C_UNDERLINE : str = "\033[4m"
    C_FLASH_1 : str = "\033[5m"
    C_FLASH_2 : str = "\033[6m"
    C_HIGHLIGHT : str = "\033[7m"
    C_HIDDEN : str = "\033[8m"
    C_CROSSED : str = "\033[9m"
    C_DARK_GREY : str = "\033[30m"
    C_DARK_RED : str = "\033[31m"
    C_DARK_GREEN : str = "\033[32m"
    C_DARK_YELLOW : str = "\033[33m"
    C_DARK_BLUE : str = "\033[34m"
    C_DARK_LAVANDA : str = "\033[35m"
    C_DARK_CYAN : str = "\033[36m"
    C_DARK_WHITE : str = "\033[37m"
    C_HIGHLIGHT_DARK_GREY : str = "\033[40m"
    C_HIGHLIGHT_DARK_RED : str = "\033[41m"
    C_HIGHLIGHT_DARK_GREEN : str = "\033[42m"
    C_HIGHLIGHT_DARK_YELLOW : str = "\033[43m"
    C_HIGHLIGHT_DARK_BLUE : str = "\033[44m"
    C_HIGHLIGHT_DARK_LAVANDA : str = "\033[45m"
    C_HIGHLIGHT_DARK_CYAN : str = "\033[46m"
    C_HIGHLIGHT_DARK_WHITE : str = "\033[47m"
    C_GREY : str = "\033[90m"
    C_RED : str = "\033[91m"
    C_GREEN : str = "\033[92m"
    C_YELLOW : str = "\033[93m"
    C_BLUE : str = "\033[94m"
    C_LAVANDA : str = "\033[95m"
    C_CYAN : str = "\033[96m"
    C_WHITE : str = "\033[97m"
    C_HIGHLIGHT_GREY : str = "\033[100m"
    C_HIGHLIGHT_RED : str = "\033[101m"
    C_HIGHLIGHT_GREEN : str = "\033[102m"
    C_HIGHLIGHT_YELLOW : str = "\033[103m"
    C_HIGHLIGHT_BLUE : str = "\033[104m"
    C_HIGHLIGHT_LAVANDA : str = "\033[105m"
    C_HIGHLIGHT_CYAN : str = "\033[106m"
    C_HIGHLIGHT_WHITE : str = "\033[107m"


    @staticmethod
    def color_fg(
            color : int
        ) -> ANSI:
        """
            Get ANSI sequence for the foreground color 'color'

            Arguments:
                color (int): color code

            Returns:
                ANSI: ansi sequence
        """

        try:
            from Console.ANSI import ANSI
        except Exception:
            raise ImportError('ANSI failed to import in Color.py')

        return ANSI(f"{ANSI.ESC}38;5;{color}m")


    @staticmethod
    def color_bg(
            color : int
        ) -> ANSI:
        """
            Get ANSI sequence for the background color 'color'

            Arguments:
                color (int): color code

            Returns:
                ANSI: ansi sequence
        """

        try:
            from Console.ANSI import ANSI
        except Exception:
            raise ImportError('ANSI failed to import in Color.py')

        return ANSI(f"{ANSI.ESC}48;5;{color}m")


    @staticmethod
    def rgb_fg(
            r : int,
            g : int,
            b : int
        ) -> ANSI:
        """
            Get ANSI sequence for the foreground color with 'r', 'g' and 'b'

            Arguments:
                r (int): red value (0->255)
                g (int): green value (0->255)
                b (int): blue value (0->255)

            Returns:
                ANSI: ansi sequence
        """

        try:
            from Console.ANSI import ANSI
        except Exception:
            raise ImportError('ANSI failed to import in Color.py')

        return ANSI(f"{ANSI.ESC}38;2;{r};{g};{b}m")


    @staticmethod
    def rgb_bg(
            r : int,
            g : int,
            b : int
        ) -> ANSI:
        """
            Get ANSI sequence for the background color with 'r', 'g' and 'b'

            Arguments:
                r (int): red value (0->255)
                g (int): green value (0->255)
                b (int): blue value (0->255)

            Returns:
                ANSI: ansi sequence
        """

        try:
            from Console.ANSI import ANSI
        except Exception:
            raise ImportError('ANSI failed to import in Color.py')

        return ANSI(f"{ANSI.ESC}48;2;{r};{g};{b}m")
