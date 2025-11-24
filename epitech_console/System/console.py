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
            start : str = "",
            end : str = "\n",
            file : Any = stdout,
            sleep : int | float | None = None
        ) -> None:
        """
            print on the console.
        """

        from epitech_console.System.time import Time

        print(f"{start}{str(value)}{end}", end="", file=file)

        if sleep:
            Time.sleep(sleep)
