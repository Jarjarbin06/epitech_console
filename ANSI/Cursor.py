#############################
###                       ###
###      Console v2.0     ###
###   ----Cursor.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

from builtins import object, any

class Cursor:
    """
        Cursor class

        Manipulate the cursor's position
    """

    @staticmethod
    def up(
            n: int = 1
        ) -> object:
        """
            Bring the cursor up 'n' lines

            Parameters:
                n (int): number of lines up

            Returns:
                str: ansi sequence
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')


        return ANSI(f"{ANSI.ESC}{n}A")

    @staticmethod
    def down(
            n: int = 1
        ) -> object:
        """
            Bring the cursor down 'n' lines

            Parameters:
                n (int): number of lines down

            Returns:
                str: ansi sequence
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}{n}B")

    @staticmethod
    def left(
            n: int = 1
        ) -> object:
        """
            Bring the cursor left 'n' column

            Parameters:
                n (int): number of column left

            Returns:
                str: ansi sequence
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}{n}D")

    @staticmethod
    def right(
            n: int = 1
        ) -> object:
        """
            Bring the cursor right 'n' column

            Parameters:
                n (int): number of column right

            Returns:
                str: ansi sequence
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}{n}C")

    @staticmethod
    def top(
        ):
        """
            Move the cursor to the top left corner of the console

            Returns:
                str: ansi sequence
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}H")

    @staticmethod
    def move(
            x : int = 0,
            y : int = 0
        ) -> object:
        """
            Move the cursor to the column x and line y

            Returns:
                str: ansi sequence
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}{y};{x}H")

    @staticmethod
    def set(
        ) -> object:
        """
            Save the cursor's position

            Returns:
                str: ansi sequence
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}s")

    @staticmethod
    def reset(
        ) -> object:
        """
            Move the cursor to the saved position

            Returns:
                str: ansi sequence
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}u")

    @staticmethod
    def show(
        ) -> object:
        """
            Show the cursor

            Returns:
                str: ansi sequence
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}?25h")

    @staticmethod
    def hide(
        ) -> object:
        """
            Hide the cursor

            Returns:
                str: ansi sequence
        """

        try:
            from ANSI import ANSI
        except Exception:
            raise ImportError('ANSI sub-modules failed to import')

        return ANSI(f"{ANSI.ESC}?25l")
