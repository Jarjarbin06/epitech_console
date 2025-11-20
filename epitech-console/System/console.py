#############################
###                       ###
###      Console v2.0     ###
###   ----Console.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object, any


class Console(object):
    """
        Console class.

        Console tool.
    """

    from sys import stdout


    @staticmethod
    def print(
            value : any = "",
            *,
            start : str = "",
            end : str = "\n",
            file : any = stdout,
            sleep : int | float | None = None
        ) -> None:
        """
            print on the console.
        """

        from Console.System.time import Time

        print(f"{start}{str(value)}{end}", end="", file=file)

        if sleep:
            Time.sleep(sleep)
