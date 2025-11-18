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


    try:
        from Console.Text import Text
    except Exception:
        raise ImportError('Text failed to import in Animation.py')


    def __init__(
            self,
            animation : list[str | Text] | str = ""
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
        self.step : int = 0


    def __add__(
            self,
            other : object | str
        ) -> object:
        """
            Add 2 Animations together.

            Parameters:
                other (Animation | str): Animation

            Returns:
                Animation: Animation
        """

        assert type(other) in [Animation, str], 'Animation can only be added with other Animation or str'

        if isinstance(other, Animation):
            return Animation(self.animation + other.animation)

        else:
            return Animation(self.animation + [other])


    def __str__(
            self
        ) -> str :
        """
            Convert Animation object to string.

            Returns:
                str: Animation string
        """

        return str(self.animation[self.step])


    def __call__(
            self
        ) -> str:
        """
            Convert Animation object to string.

            Returns:
                str: Animation string
        """
