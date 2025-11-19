#############################
###                       ###
###      Console v2.0     ###
###    ----Color.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object


class Color(object):
    """
        Color class.

        ANSI coloring system.

        Attributes:
            C_RESET (int): Base color.
            C_BOLD (int): Bold color.
            C_DARK_BASE (int): Dark base color.
            C_ITALIC (int): Italic color.
            C_UNDERLINE (int): Underline color.
            C_FLASH_1 (int): Flash color.
            C_FLASH_2 (int): Flash color.
            C_HIGHLIGHT (int): Highlight color.
            C_HIDDEN (int): Hidden color.
            C_CROSSED (int): Crossed color.
            C_DARK_GREY (int): Dark grey color.
            C_DARK_RED (int): Dark red color.
            C_DARK_GREEN (int): Dark green color.
            C_DARK_YELLOW (int): Dark yellow color.
            C_DARK_BLUE (int): Dark blue color.
            C_DARK_LAVANDA (int): Dark lavanda color.
            C_DARK_CYAN (int): Dark cyan color.
            C_DARK_WHITE (int): Dark white color.
            C_HIGHLIGHT_DARK_GREY (int): Highlight dark grey color.
            C_HIGHLIGHT_DARK_RED (int): Highlight dark red color.
            C_HIGHLIGHT_DARK_GREEN (int): Highlight dark green color.
            C_HIGHLIGHT_DARK_YELLOW (int): Highlight dark yellow color.
            C_HIGHLIGHT_DARK_BLUE (int): Highlight dark blue color.
            C_HIGHLIGHT_DARK_LAVANDA (int): Highlight dark lavanda color.
            C_HIGHLIGHT_DARK_CYAN (int): Highlight dark cyan color.
            C_HIGHLIGHT_DARK_WHITE (int): Highlight dark white color.
            C_GREY (int): Grey color.
            C_RED (int): Red color.
            C_GREEN (int): Green color.
            C_YELLOW (int): Yellow color.
            C_BLUE (int): Blue color.
            C_LAVANDA (int): Lavanda color.
            C_CYAN (int): Cyan color.
            C_WHITE (int): White color.
            C_HIGHLIGHT_GREY (int): Highlight grey color.
            C_HIGHLIGHT_RED (int): Highlight red color.
            C_HIGHLIGHT_GREEN (int): Highlight green color.
            C_HIGHLIGHT_YELLOW (int): Highlight yellow color.
            C_HIGHLIGHT_BLUE (int): Highlight blue color.
            C_HIGHLIGHT_LAVANDA (int): Highlight lavanda color.
            C_HIGHLIGHT_CYAN (int): Highlight cyan color.
            C_HIGHLIGHT_WHITE (int): Highlight white color.
    """

    from Console.ANSI.ansi import ANSI

    C_RESET : int = 0
    C_BOLD : int = 1
    C_DARK_BASE : int = 2
    C_ITALIC : int = 3
    C_UNDERLINE : int = 4
    C_FLASH_1 : int = 5
    C_FLASH_2 : int = 6
    C_HIGHLIGHT : int = 7
    C_HIDDEN : int = 8
    C_CROSSED : int = 9
    C_DARK_GREY : int = 30
    C_DARK_RED : int = 31
    C_DARK_GREEN : int = 32
    C_DARK_YELLOW : int = 33
    C_DARK_BLUE : int = 34
    C_DARK_LAVANDA : int = 35
    C_DARK_CYAN : int = 36
    C_DARK_WHITE : int = 37
    C_HIGHLIGHT_DARK_GREY : int = 40
    C_HIGHLIGHT_DARK_RED : int = 41
    C_HIGHLIGHT_DARK_GREEN : int = 42
    C_HIGHLIGHT_DARK_YELLOW : int = 43
    C_HIGHLIGHT_DARK_BLUE : int = 44
    C_HIGHLIGHT_DARK_LAVANDA : int = 45
    C_HIGHLIGHT_DARK_CYAN : int = 46
    C_HIGHLIGHT_DARK_WHITE : int = 47
    C_GREY : int = 90
    C_RED : int = 91
    C_GREEN : int = 92
    C_YELLOW : int = 93
    C_BLUE : int = 94
    C_LAVANDA : int = 95
    C_CYAN : int = 96
    C_WHITE : int = 97
    C_HIGHLIGHT_GREY : int = 100
    C_HIGHLIGHT_RED : int = 101
    C_HIGHLIGHT_GREEN : int = 102
    C_HIGHLIGHT_YELLOW : int = 103
    C_HIGHLIGHT_BLUE : int = 104
    C_HIGHLIGHT_LAVANDA : int = 105
    C_HIGHLIGHT_CYAN : int = 106
    C_HIGHLIGHT_WHITE : int = 107


    @staticmethod
    def color(
            color: int
        ) -> ANSI:
        """
            Get ANSI sequence from the 'color'

            Arguments:
                color (str): color code

            Returns:
                ANSI: ansi sequence
        """

        from Console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}{str(color)}m")


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

        from Console.ANSI.ansi import ANSI

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

        from Console.ANSI.ansi import ANSI

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

        from Console.ANSI.ansi import ANSI

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

        from Console.ANSI.ansi import ANSI

        return ANSI(f"{ANSI.ESC}48;2;{r};{g};{b}m")
