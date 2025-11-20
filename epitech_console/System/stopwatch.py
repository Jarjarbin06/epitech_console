#############################
###                       ###
###    Epitech Console    ###
###  ----Stopwatch.py---- ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object


class StopWatch(object):
    """
        StopWatch class.

        StopWatch tool.
    """


    def __init__(
            self,
            start : bool = False,
        ) -> None:
        """
            Create a stopwatch.
        """

        self.start_time : float = 0.0
        self.time : float = 0.0

        if start:
            self.start()


    def __str__(
            self
        ) -> str :
        """
            Convert StopWatch object to string.

            Returns:
                str: StopWatch string
        """

        return str(self.elapsed())


    def start(
            self
        ) -> None:
        """
            Start the stopwatch.
        """

        from time import time

        self.start_time = time()


    def stop(
            self
        ) -> None:

        self.update()
        self.start_time = 0.0


    def update(
            self
        ) -> None:
        """
            Update the stopwatch.
        """

        from time import time

        if self.start_time:
            self.time = time() - self.start_time


    def elapsed(
            self
        ) -> float:
        """
            Get elapsed time.

            Returns:
                float: Elapsed time.
        """

        return self.time


    def reset(
            self
        ) -> None:
        """
            Reset the stopwatch.
        """

        self.stop()
        self.start()
