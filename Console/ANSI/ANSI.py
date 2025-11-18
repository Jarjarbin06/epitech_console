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


    try:
        from Console.ANSI import ANSI
    except Exception:
        raise ImportError('Line sub-modules failed to import')


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
        ) -> ANSI:
        """
            Add 2 ANSI sequences together.

            Parameters:
                other (ANSI | str): ANSI sequence

            Returns:
                ANSI: ANSI sequence
        """

        assert type(other) in [ANSI, str], 'ANSI can only be added with other ANSI or str'

        if isinstance(other, ANSI):
            return ANSI(f"{self.sequence}{other.sequence}")

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
