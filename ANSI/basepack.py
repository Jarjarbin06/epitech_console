#############################
###                       ###
###    Epitech Console    ###
###  ----BasePack.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object


class BasePack(object):
    """
        BasePack class.

        Base animation pack ready for use.

        Attributes:
            P_ERROR (tuple): error tuple of color.
            P_WARNING (tuple): warning tuple of color.
            P_OK (tuple): validation tuple of color.
            P_INFO (tuple): information tuple of color.
    """


    P_ERROR = (0, 0)
    P_WARNING = (0, 0)
    P_OK = (0, 0)
    P_INFO = (0, 0)


    @staticmethod
    def update(
        ) -> None:
        """
            Initialise the BasePack class
        """

        from epitech_console.ANSI.color import Color

        BasePack.P_ERROR = (Color.C_BG_DARK_RED, Color.C_FG_DARK_RED)
        BasePack.P_WARNING = (Color.C_BG_DARK_YELLOW, Color.C_FG_DARK_YELLOW)
        BasePack.P_OK = (Color.C_BG_DARK_GREEN, Color.C_FG_DARK_GREEN)
        BasePack.P_INFO = (Color.C_BG, Color.C_RESET)
