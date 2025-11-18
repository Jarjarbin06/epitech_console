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


    try:
        from Console.ANSI import ANSI
    except Exception:
        raise ImportError('ANSI failed to import in Text.py')

    try:
        from Console.Text import Text
    except Exception:
        raise ImportError('Text failed to import in Text.py')


    def __init__(
            self,
            text : ANSI | str = ""
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
            other : ANSI | str
        ) -> Text:
        """
            Add 2 Animations together.

            Parameters:
                other (Animation | str): Animation

            Returns:
                Animation: Animation
        """

        try:
            from Console.ANSI import ANSI
        except Exception:
            raise ImportError('ANSI failed to import in Text.py')

        assert type(other) in [Text, ANSI, str], 'Text can only be added with other Text or str'

        if isinstance(other, Text):
            return Text(f"{self.text}{other.text}")

        elif isinstance(other, ANSI):
            return Text(f"{self.text}{other.sequence}")

        else:
            return Text(f"{self.text}{other}")


    def __str__(
            self
        ) -> str :
        """
            Convert Animation object to string.

            Returns:
                str: Animation string
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

