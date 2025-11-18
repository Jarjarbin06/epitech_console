#############################
###                       ###
###      Console v2.0     ###
###    ----Error.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


class Error(Exception):
    """
    Error class.

    Error for Console.
    """


    def __init__(
            self,
            message : str = "an error occurred",

            *,
            error : str = "Error",
            link : tuple[str, int] | None = None
        ) -> None:
        """
            Create an Error.

            Parameters:
                message (str): The error message.
                link (tuple[str, int]): The link to where the error comes from (file and line).
        """

        try:
            from Console.Text import Text
        except Exception:
            raise ImportError('Text failed to import in Error.py')

        self.message : str = ""
        self.error : str = ""
        self.link : str | None = None

        self.message = message
        self.error = error
        if link:
            self.link = Text.clion_link(link[0], link[1])


    def __str__(
            self
        ) -> str:
        """
            Get string representation of the error.

            Returns:
                str: String representation of the error.
        """

        return f"{self.error}:\n    {self.message}\n\n{self.link}"
