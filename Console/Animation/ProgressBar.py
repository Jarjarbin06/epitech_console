#############################
###                       ###
###      Console v2.0     ###
### ----ProgressBar.py----###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


class ProgressBar:
    """
        ProgressBar class.

        Progress-bar tool.
    """

    try:
        from Console.Animation import Animation
        from Console.Animation.Style import Style
    except Exception:
        raise ImportError('failed import in ProgressBar.py')


    def __init__(
            self,
            length : int,

            *,
            style : Style = Style("#", "-", "<", ">", "|", "|"),
            color : object | None = None,
            percent_style : str = "bar",
            spinner : object | None = None,
            spinner_position : str = "s"
        ) -> None:
        """
            Create a Progress-bar object.

            Parameters:
                length (int): Progress bar length.

                style (Style)(optional): Progress bar style.
                color (Color | None)(optional): Progress bar color.
                percent_style (str)(optional): Progress bar percent style (num/bar/mix).
                spinner (Spinner | None)(optional): Progress bar spinner.
                spinner_position (str)(optional): Progress bar spinner position (s/e).
        """

        try:
            from Console.ANSI import ANSI, Color
            from Console.Animation import Animation, Spinner
        except Exception:
            raise ImportError('Animation failed to import in ProgressBar.py')

        if not color:
            color = ANSI(Color.C_RESET)



        self.animation : Animation = Animation()
        self.percent : int | float = 0
        self.percent_style : str = percent_style
        self.spinner : Animation | None = spinner
        self.spinner_position : str = spinner_position


    def __getitem__(
            self,
            item : int
        ) -> str :
        """
            Get the current step of the animations and convert it to a string.

            Returns:
                str: Animations string
        """

        return str(self.animation[item])


    def __str__(
            self
        ) -> str :
        """
            Convert ProgressBar object to string.

            Returns:
                str: ProgressBar string
        """

        return self[self.animation.step]


    def __call__(
            self
        ) -> None:
        """
            Do a step of the animations.
        """

        self.update()


    def update(
            self,
            *,
            auto_reset: bool = False
        ) -> None:
        """
            Do a step of the animations.
        """

        if self.spinner :
            self.spinner.update(auto_reset=auto_reset)

        self.animation.update(auto_reset=auto_reset)


    def render(
            self,
            *,
            delete : bool = False
        ) -> str:
        """
            Convert ProgressBar object to string.

            Returns:
                str: ProgressBar string
        """

        try:
            from Console.ANSI import Line
        except Exception:
            raise ImportError('failed import in ProgressBar.py')

        return Line.clear_previous_line() + str(self)
