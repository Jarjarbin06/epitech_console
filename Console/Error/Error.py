#############################
###                       ###
###      Console v2.0     ###
###    ----Error.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


class Error(Exception):


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

        self.message : str = ""
        self.error : str = ""
        self.link : str | None = None

        self.message = message
        self.error = error
        if link:
            self.link = Error.clion_link(link[0], link[1])

    def __str__(
            self
        ) -> str:
        """
            Get string representation of the error.

            Returns:
                str: String representation of the error.
        """

        return f"{self.error}:\n    {self.message}\n\n{self.link}"

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
