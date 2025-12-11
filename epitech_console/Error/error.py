#############################
###                       ###
###    Epitech Console    ###
###    ----error.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any


class Error(Exception):
    """
    Error class.

    Error for epitech_console.
    """


    def __init__(
            self,
            message : str = "an error occurred",

            *,
            error : str = "Error",
            link : tuple[str , int] | None = None
        ) -> None:
        """
            Create an Error.

            Parameters:
                message (str, optional): The error message.
                error (str, optional): The error type (title).
                link (tuple[str, int], optional): The link to where the error comes from (file and line).
        """

        self.message : str = message
        self.error : str = error
        self.link_data : tuple[str, int] | None = link
        self.link : str | None = None

        self.create_link()


    def create_link(
            self
        ) -> None:
        """
            Create an error link.
            Create an error link.
        """

        from epitech_console.Text.text import Text

        if self.link_data:
            if len(self.link_data) == 1 and type(self.link_data[0]) in [str]:
                self.link = Text.file_link(self.link_data[0])
            if len(self.link_data) == 2 and type(self.link_data[0]) in [str] and type(self.link_data[1]) in [int]:
                if self.link_data[1] > 0:
                    self.link = Text.file_link(self.link_data[0], self.link_data[1])


    def __str__(
            self
        ) -> str:
        """
            Get string representation of the error.

            Returns:
                str: String representation of the error.
        """

        return f'{self.error}:\n    {self.message}\n\n{self.link if self.link else ""}'


    def __repr__(
            self
        ) -> str:
        """
            Convert Error object to string.

            Returns:
                str: Error string
        """

        return f"Error(\"{self.message}\", error=\"{self.error}\", link={self.link_data})"


class ErrorImport(Error):
    """
        ErrorImport class.

        Import Error.
    """


class ErrorAttribute(Error):
    """
        ErrorAttribute class.

        Attribute Error.
    """


class ErrorType(Error):
    """
        ErrorType class.

        Type Error.
    """


class ErrorName(Error):
    """
        ErrorName class.

        Name Error.
    """


class ErrorValue(Error):
    """
        ErrorValue class.

        Value Error.
    """
