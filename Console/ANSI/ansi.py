#############################
###                       ###
###      Console v2.0     ###
###    ----ANSI.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object


class ANSI(object):
    """
        ANSI class.

        ANSI string tool.

        Attributes:
            ESC (str) : ANSI escape (ANSI sequence starter).
    """


    ESC: str = "\033["


    def __init__(
            self,
            sequence : list[object | str] | str = ""
        ) -> None:
        """
            Create an ANSI sequence.

            Parameters:
                sequence (list[ANSI | str] | str): ANSI sequence
        """

        self.sequence : str = ""

        if type(sequence) in [list]:
            for item in sequence:
                self.sequence += str(item)

        else:
            self.sequence = sequence


    def __add__(
            self,
            other : object | str
        ) -> object:
        """
            Add 2 ANSI sequences together.

            Parameters:
                other (ANSI | Animation | StopWatch | ProgressBar | Text | str): ANSI sequence

            Returns:
                ANSI: ANSI sequence
        """

        from Console.Animation.animation import Animation
        from Console.Animation.progressbar import ProgressBar
        from Console.Text.text import Text
        from Console.System.stopwatch import StopWatch

        if type(other) in [ANSI]:
            return ANSI(f"{self.sequence}{other.sequence}")

        elif type(other) in [Animation, StopWatch, ProgressBar, Text, str]:
            return ANSI(f"{self.sequence}{str(other)}")

        else:
            return ANSI("")


    def __str__(
            self
        ) -> str :
        """
            Convert ANSI object to string.

            Returns:
                str: ANSI string
        """

        return str(self.sequence)
