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
from epitech_console.System.setting import Setting


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
                self.link = str(Text.file_link(self.link_data[0]))
            if len(self.link_data) == 2 and type(self.link_data[0]) in [str] and type(self.link_data[1]) in [int]:
                if self.link_data[1] > 0:
                    self.link = str(Text.file_link(self.link_data[0], self.link_data[1]))


    @staticmethod
    def _lauch_message(
        ) -> str:
        """
            Returns lauch error message.

            Return:
                str: Lauch error message.
        """

        from epitech_console.ANSI.color import Color

        return (
            f"{Color.color(Color.C_BG_YELLOW)} {Color.color(Color.C_RESET)} {Color.color(Color.C_FG_YELLOW)}epitech_console launched with error{Color.color(Color.C_RESET)}\n"
            f"{Color.color(Color.C_BG_YELLOW)} {Color.color(Color.C_RESET)}\n"
            f"{Color.color(Color.C_BG_YELLOW)} {Color.color(Color.C_RESET)} {Color.color(Color.C_FG_YELLOW)}Please reinstall with :{Color.color(Color.C_RESET)}\n"
            f"{Color.color(Color.C_BG_YELLOW)} {Color.color(Color.C_RESET)} {Color.color(Color.C_FG_YELLOW)}    'pip install --upgrade --force-reinstall epitech_console'{Color.color(Color.C_RESET)}\n"
            f"{Color.color(Color.C_BG_YELLOW)} {Color.color(Color.C_RESET)}\n"
            f"{Color.color(Color.C_BG_YELLOW)} {Color.color(Color.C_RESET)} {Color.color(Color.C_FG_YELLOW)}Please report the issue here : https://github.com/Jarjarbin06/epitech_console/issues{Color.color(Color.C_RESET)}\n"
        )


    def __str__(
            self,
        ) -> str:
        """
            Get string representation of the error.

            Returns:
                str: String representation of the error.
        """

        from epitech_console.ANSI.color import Color

        string : str = (f"{Color.color(Color.C_BG_RED)} {Color.color(Color.C_RESET)} {Color.color(Color.C_FG_RED)}" if Setting.S_SETTING_AUTO_COLOR else "") + self.error + ":"

        for line in self.message.splitlines():
            string += "\n" + (f"{Color.color(Color.C_BG_RED)} {Color.color(Color.C_RESET)}     {Color.color(Color.C_FG_RED)}" if Setting.S_SETTING_AUTO_COLOR else "") + self.message

        string += (f"{Color.color(Color.C_BG_RED)} {Color.color(Color.C_RESET)} {Color.color(Color.C_FG_RED)}" if Setting.S_SETTING_AUTO_COLOR else "") + ("\n{Color.color(Color.C_BG_RED)} {Color.color(Color.C_RESET)}\n{Color.color(Color.C_BG_RED)} {Color.color(Color.C_RESET)}  {Color.color(Color.C_FG_RED)}" + self.link) if self.link else ""

        return string + "\n"


    def __repr__(
            self
        ) -> str:
        """
            Convert Error object to string.

            Returns:
                str: Error string
        """

        return f"Error(\"{self.message}\", error=\"{self.error}\", link={self.link_data})"


class ErrorLaunch(Error):
    """
        ErrorLaunch class.

        Launch Error.
    """


    def __init__(
            self,
            message : str = "an error occurred during the launch",

            *,
            error : str = "ErrorLaunch",
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


class ErrorImport(Error):
    """
        ErrorImport class.

        Import Error.
    """


    def __init__(
            self,
            message : str = "an error occurred during an import",

            *,
            error : str = "ErrorImport",
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


class ErrorType(Error):
    """
        ErrorType class.

        Type Error.
    """


    def __init__(
            self,
            message : str = "an error occurred on a type",

            *,
            error : str = "ErrorType",
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


class ErrorValue(Error):
    """
        ErrorValue class.

        Value Error.
    """


    def __init__(
            self,
            message : str = "an error occurred on a value",

            *,
            error : str = "ErrorValue",
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
