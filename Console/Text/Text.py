#############################
###                       ###
###      Console v2.0     ###
###    ----Text.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


class Text:
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

        try:
            from Console.ANSI import ANSI
        except Exception:
            raise ImportError('ANSI failed to import in Text.py')

        self.text : str = ""
        assert type(text) in [ANSI, str], 'text must be of type ANSI or str'

        if isinstance(text, ANSI):
            self.text = text.sequence

        else :
            self.text = text


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

        try:
            from Console.ANSI import ANSI
            from Console.Animation import Animation
        except Exception:
            raise ImportError('ANSI failed to import in Text.py')

        assert type(other) in [Text, Animation, ANSI, str], 'Text can only be added with other Text, Animation, ANSI or str'

        if isinstance(other, Text):
            return Text(f"{self.text}{other.text}")

        elif isinstance(other, ANSI):
            return Text(f"{self.text}{other.sequence}")

        elif isinstance(other, Animation):
            return Text(f"{self.text}{str(other)}")

        else:
            return Text(f"{self.text}{other}")


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
