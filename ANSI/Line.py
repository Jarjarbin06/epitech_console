#############################
###                       ###
###      Console v2.0     ###
###     ----Line.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

from builtins import object, any

class Line:
    """
        Line class.

        Manipulate the lines of the console.
    """

    @staticmethod
    def clear_line(
        ) -> object:
        """
            Clear the current line

            Returns:
                ANSI: ansi sequence
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}2K")

    @staticmethod
    def clear_start_line(
        ) -> object:
        """
            Clear the current line from the start to the cursor's position

            Returns:
                ANSI: ansi sequence
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}1K")

    @staticmethod
    def clear_end_line(
    ) -> object:
        """
            Clear the current line from the cursor's position to the end

            Returns:
                ANSI: ansi sequence
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}K")

    @staticmethod
    def clear_screen(
        ) -> object:
        """
            Clear the screen

            Returns:
                ANSI: ansi sequence
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}2J")

    @staticmethod
    def clear(
        ) -> object:
        """
            Clear the screen and bring the cursor to the top left corner

            Returns:
                ANSI: ansi sequence
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI.clear_screen() + ANSI.top()
