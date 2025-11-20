#############################
###                       ###
###    Epitech Console    ###
###    ----Text.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from epitech_console.Text.format import Format


class Text(Format):
    """
        Text class.

        Text tool.
    """


    def __init__(
            self,
            text : object | str = ""
        ) -> None:
        """
            Create a text.

            Parameters:
                text (ANSI | str): text
        """

        from epitech_console.ANSI.ansi import ANSI

        self.text : str = ""

        if type(text) in [ANSI]:
            self.text = text.sequence

        else :
            self.text = str(text)


    def __add__(
            self,
            other : object | str
        ) -> object:
        """
            Add 2 Texts together.

            Parameters:
                other (ANSI | Text | str): text

            Returns:
                Text: text
        """

        return Text(str(self) + str(other))


    def __str__(
            self
        ) -> str :
        """
            Convert Text object to string.

            Returns:
                str: Text string
        """

        return str(self.text)


    @staticmethod
    def clion_link(
            path: str,
            line: int | None = None
        ) -> str:
        """
            Get CLion link to line 'line' of the file 'path'.

            Parameters:
                path (str): Path to the file.
                line (int): Line of the file.

            Returns:
                str: CLion link.
        """

        if line:
            return f'\033]8;;jetbrains://clion/navigate/reference?file={path}&line={line}\033\\File "{path}", line {line}\033]8;;\033\\'
        else:
            return f'\033]8;;jetbrains://clion/navigate/reference?file={path}\033\\"{path}"\033]8;;\033\\'
