#############################
###                       ###
###      Console v2.0     ###
###    ----ANSI.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


class ANSI:
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
        assert type(sequence) in [str, list], 'sequence must be of type str or list[str|ANSI]'

        if isinstance(sequence, list):
            for item in sequence:
                assert type(item) in [str, ANSI], 'sequence must be of type str or list[str|ANSI]'
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
                other (ANSI | str): ANSI sequence

            Returns:
                ANSI: ANSI sequence
        """

        try:
            from Console.Animation import Animation, ProgressBar
            from Console.Text import Text
        except Exception:
            raise ImportError('failed import in ANSI.py')

        assert type(other) in [ANSI, Animation, ProgressBar, Text, str], 'ANSI can only be added with other ANSI, Text, Animation or str'

        if isinstance(other, ANSI):
            return ANSI(f"{self.sequence}{other.sequence}")

        elif isinstance(other, Animation):
            return ANSI(f"{self.sequence}{str(other)}")

        elif isinstance(other, ProgressBar):
            return ANSI(f"{self.sequence}{str(other)}")

        elif isinstance(other, Text):
            return ANSI(f"{self.sequence}{str(other)}")

        else:
            return ANSI(f"{self.sequence}{other}")


    def __str__(
            self
        ) -> str :
        """
            Convert ANSI object to string.

            Returns:
                str: ANSI string
        """

        return str(self.sequence)
