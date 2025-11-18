#############################
###                       ###
###      Console v2.0     ###
###  ----Animation.py---- ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


class Animation:
    """
        Animation class.

        Animation tool.
    """


    def __init__(
            self,
            animation : list[str | object] | str = ""
        ) -> None:
        """
            Create an animation.

            Parameters:
                animation (list[str] | str): list of step
        """

        try:
            from Console.Text import Text
        except Exception:
            raise ImportError('Text failed to import in Animation.py')

        self.animation : list[str] = []
        assert type(animation) in [str, list], 'animation must be of type str or list[str | Text]'

        if isinstance(animation, list):
            for step in animation:
                assert type(step) in [str, Text], 'animation must be of type str or list[str | Text]'
                self.animation.append(str(step))

        else:
            self.animation = [animation]

        self.length : int = len(self.animation)
        self.animation += [""]
        self.step : int = 0


    def __add__(
            self,
            other : object | str
        ) -> object:
        """
            Add 2 Animations together.

            Parameters:
                other (Animation | ANSI | Text | StopWatch | str): Animation

            Returns:
                Animation: Animation
        """

        try:
            from Console.Text import Text
            from Console.ANSI import ANSI
            from Console.System import Stopwatch
        except Exception:
            raise ImportError('failed import in Animation.py')

        assert type(other) in [Animation, ANSI, Text, Stopwatch, str]

        if isinstance(other, Animation):
            return Animation(self.animation + other.animation)

        elif isinstance(other, (Text, Stopwatch, ANSI, str)):
            return Animation(self.animation + [str(other)])


    def __getitem__(
            self,
            item : int
        ) -> str :
        """
            Get the current step of the animation and convert it to a string.

            Returns:
                str: Animation string
        """

        return str(self.animation[item])


    def __str__(
            self
        ) -> str :
        """
            Convert Animation object to string.

            Returns:
                str: Animation string
        """

        return str(self[self.step])


    def __call__(
            self,
        ) -> None:
        """
            Do a step of the animation.
        """

        self.update(True)


    def update(
            self,
            *,
            auto_reset: bool = False
        ) -> None:
        """
            Add a step to the animation.

            Parameters:
                auto_reset (bool): Automatically reset the animation. Defaults to False.
        """

        step: str = str(self)

        self.step += 1

        if self.is_last() and auto_reset:
            self.reset()

        return None


    def render(
            self,
            *,
            delete : bool = False
        ) -> str:
        """
            Convert Animation object to string.

            Returns:
                str: Animation string
        """

        try:
            from Console.ANSI import Line
        except Exception:
            raise ImportError('failed import in Animation.py')

        return Line.clear_previous_line() + str(self)


    def is_last(
            self
        ) -> bool:
        """
            Return whether it is or not the last step of the animation.

            Returns:
                bool: is the last step
        """

        return self.step >= self.length

    def reset(
            self
        ) -> None:
        """
            Reset the animation.
        """

        self.step = 0
