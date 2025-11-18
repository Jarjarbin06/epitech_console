#############################
###                       ###
###      Console v2.0     ###
###  ----Stopwatch.py---- ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


class StopWatch:
    """
        StopWatch class.

        StopWatch tool.
    """


    def __init__(
            self
        ) -> None:
        """
            Create a stopwatch.
        """

        self.start_time : float = 0.0
        self.time : float = 0.0


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
        self.update()


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
            Elapse the stopwatch.
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
