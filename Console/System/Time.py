#############################
###                       ###
###      Console v2.0     ###
###    ----Time.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


class Time:
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

        try:
            from time import sleep
        except Exception:
            raise ImportError('time failed to import in Time.py')

        sleep(seconds)
