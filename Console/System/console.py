#############################
###                       ###
###      Console v2.0     ###
###   ----Console.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object


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
            start = "",
            end = "\n",
            file = stdout,

        ) -> None:
        """
            print on the console.
        """

        print(f"{start}{str(value)}{end}", end="", file=file)
