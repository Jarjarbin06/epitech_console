#############################
###                       ###
###    Epitech Console    ###
###   ----console.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any


class Console:
    """
        Console class.

        Console tool.
    """


    from sys import stdout


    @staticmethod
    def print(
            value : Any = "",
            *,
            separator : str = " ",
            start : str = "",
            end : str = "\n",
            file : Any = stdout,
            sleep : int | float | None = None
        ) -> None:
        """
            print on the console.

            Parameters:
                value : Any value to print.
                separator (str)(optional) : Separator to use between values.
                start (str)(optional) : Start value to use for print.
                end (str)(optional) : End value to use for print.
                file (Any)(optional) : File object to use for print.
                sleep (int | float | None)(optional) : Sleep time in seconds.
        """

        from epitech_console.System.time import Time

        print(f"{start}{str(value)}{end}", end="", file=file)

        if sleep:
            Time.wait(sleep)


    @staticmethod
    def input(
            msg : str = "Input : "
        ) -> str:
        """
            Get user text input from the console.

            Parameters:
                msg (str) : Message to show when user enters input.
        """

        return input(msg)

    @staticmethod
    def flush(
            stream : Any = stdout,
        ) -> None:
        """
            Flush console output.

            Parameters:
                stream (Any)(optional) : Stream object to be flushed (generally stdin, stdout and stderr).
        """

        stream.flush()
