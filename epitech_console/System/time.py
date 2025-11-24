#############################
###                       ###
###    Epitech Console    ###
###    ----time.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object


class Time(object):
    """
        Time class.

        Time tool.
    """

    @staticmethod
    def sleep(
            seconds : int | float
        ) -> None:
        """
        """

        from time import sleep

        sleep(seconds)
