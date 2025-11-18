#############################
###                       ###
###      Console v2.0     ###
###     ----Line.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


class Line:
    """
        Line class.

        Manipulate the lines of the console.
    """


    try:
        from Console.ANSI import ANSI
    except Exception:
        raise ImportError('Line sub-modules failed to import')


    @staticmethod
    def clear_line(
        ) -> ANSI:
        """
            Clear the current line

            Returns:
                ANSI: ansi sequence
        """

        try:
            from Console.ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}2K")


    @staticmethod
    def clear_start_line(
        ) -> ANSI:
        """
            Clear the current line from the start to the cursor's position

            Returns:
                ANSI: ansi sequence
        """

        try:
            from Console.ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}1K")


    @staticmethod
    def clear_end_line(
    ) -> ANSI:
        """
            Clear the current line from the cursor's position to the end

            Returns:
                ANSI: ansi sequence
        """

        try:
            from Console.ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}K")


    @staticmethod
    def clear_screen(
        ) -> ANSI:
        """
            Clear the screen

            Returns:
                ANSI: ansi sequence
        """

        try:
            from Console.ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}2J")


    @staticmethod
    def clear(
        ) -> ANSI:
        """
            Clear the screen and bring the cursor to the top left corner

            Returns:
                ANSI: ansi sequence
        """

        try:
            from Console.ANSI import Line, Cursor
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return Line.clear_screen() + Cursor.top()
