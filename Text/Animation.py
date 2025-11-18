#############################
###                       ###
###      Console v2.0     ###
###  ----Animation.py---- ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


class Animation(object):
    """
        Animation class.

        Animation tool.
    """


    try:
        pass
    except Exception:
        raise ImportError('Animation sub-modules failed to import')


    def __init__(
            self,
            animation : list[str] | str = ""
        ) -> None:
        """
            Create an animation.

            Parameters:
                animation (list[str] | str): list of step
        """

        self.animation : list[str] = []
        assert type(animation) in [str, list], 'animation must be of type str or list[str]'

        if isinstance(animation, list):
            for step in animation:
                assert type(step) in [str], 'animation must be of type str or list[str]'
                self.animation.append(step)

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
            return Animation(f"{self.animation}{other.animation}")

        else:
            return Animation(f"{self.animation}{other}")


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
