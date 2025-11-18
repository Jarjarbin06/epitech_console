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
            message : str = "an error occurred"
        ) -> None:
        """
            Create an Error.
        """

        self.message = message

    def __str__(
            self
        ) -> str:
        """
            Get string representation of the error.
        """

        return str(self.message)

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
            return f"\033]8;;jetbrains://clion/navigate/reference?file={path}&line={line}\033\\{path}:{line}\033]8;;\033\\"
        else:
            return f"\033]8;;jetbrains://clion/navigate/reference?file={path}\033\\{path}\033]8;;\033\\"
