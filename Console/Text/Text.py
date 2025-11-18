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
        from Console.Text import Animation
    except Exception:
        raise ImportError('Text sub-modules failed to import')


    def __init__(
            self,
            text : str = ""
        ) -> None:
        """
            Create a text.

            Parameters:
                text (str): text
        """

        self.text : str = ""
        assert type(text) in [str], 'text must be of type str'

        self.text = text


    def __add__(
            self,
            other : object | str
        ) -> object:
        """
            Add 2 Animations together.

            Parameters:
                other (Animation | str): Animation

            Returns:
                Animation: Animation
        """

        assert type(other) in [Text, str], 'Text can only be added with other Text or str'

        if isinstance(other, Text):
            return Text(f"{self.text}{other.text}")

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
