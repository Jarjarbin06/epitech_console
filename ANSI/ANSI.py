#############################
###                       ###
###      Console v2.0     ###
###    ----ANSI.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

from builtins import object, any

try:
    from Cursor import Cursor
    from Line import Line
    from Color import Color
except Exception:
    raise ImportError('ANSI sub-modules failed to import')

class ANSI(Cursor, Line, Color):
    """
    """

    ESC: str = "\033["

    def __init__(
            self,
            sequence : list[object | str] | str = ""
        ) -> None:
        """
            create an ANSI sequence

            Parameters:
                sequence (list[ANSI | str] | str): ANSI sequence
        """

        self.sequence : str = ""
        assert type(sequence) in [str, list], 'sequence must be of type str or list[str|ANSI]'

        if isinstance(sequence, str):
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
        """

        return str(self.sequence)
