#############################
###                       ###
###      Console v2.0     ###
###    ----Time.py----    ###
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
