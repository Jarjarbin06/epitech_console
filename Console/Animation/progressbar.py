#############################
###                       ###
###      Console v2.0     ###
### ----ProgressBar.py----###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object


def create_progress_bar(
        length,
        style
    ) -> list[str]:
    """
        Create the Progress-bar animation.
    """

    animation : list[str] = []

    for y in range(length):
        animation += [style.border_left]

        for x in range(y):
            animation[y] += style.on

        animation[y] += style.arrow_right

        for x in range((length - y) - 1):
            animation[y] += style.off

        animation[y] = animation[y][0:-1] + style.border_right

    return animation


class ProgressBar(object):
    """
        ProgressBar class.

        Progress-bar tool.
    """

    from Console.Animation.animation import Animation
    from Console.ANSI.color import Color
    from Console.Animation.style import Style


    def __init__(
            self,
            length : int,

            *,
            style : object = Style("#", "-", "<", ">", "|", "|"),
            percent_style : str = "bar",
            spinner : Animation | None = None,
            spinner_position : str = "s"
        ) -> None:
        """
            Create a Progress-bar object.

            Parameters:
                length (int): Progress bar length.

                style (Style | None)(optional): Progress bar style.
                percent_style (str)(optional): Progress bar percent style (num/bar/mix).
                spinner (Animation | None)(optional): Progress bar spinner.
                spinner_position (str)(optional): Progress bar spinner position (s/e).
        """

        from Console.Animation.animation import Animation

        self.length = length
        self.animation : Animation = Animation(create_progress_bar(length, style))
        self.percent : int | float = 0
        self.percent_style : str = percent_style
        self.spinner : Animation | None = spinner
        self.spinner_position : str = spinner_position


    def __getitem__(
            self,
            item : int,
            *,
            color : int = Color.C_RESET
        ) -> str :
        """
            Get the current step of the animations and convert it to a string.

            Parameters:
                item (int): Step number
                color (int)(optional): Color

            Returns:
                str: Animations string
        """

        return str(self.animation[item])


    def __str__(
            self,
            *,
            color : tuple[int, int, int] = (Color.C_RESET, Color.C_RESET, Color.C_RESET),
            hide_spinner : bool = False
        ) -> str :
        """
            Convert ProgressBar object to string.

            Parameters:
                color (tuple[int, int, int])(optional): Color
                hide_spinner (bool): hide the spinner

            Returns:
                str: ProgressBar string
        """

        from Console.ANSI.color import Color

        string : str = ""

        if self.percent_style in ["bar", "mix"] :
            idx : int = int((self.percent / 100) * self.length)

            if idx >= self.length:
                idx = self.length - 1

            string += self.__getitem__(idx, color=color[0])

        if self.spinner and not hide_spinner :
            string += self.spinner.__str__(color=color[1])

        if self.percent_style in ["num", "mix"] :
            string += f" {Color.color(color[2])}{str(self.percent)}%{Color.color(Color.C_RESET)}"

        return string


    def __call__(
            self
        ) -> None:
        """
            Do a step of the animations.
        """

        self.update()


    def update(
            self,
            percent : int = 0,
            *,
            update_spinner : bool = True,
            auto_reset: bool = True
        ) -> None:
        """
            Do a step of the animations.

            Parameters:
                percent (int): Percentage
                update_spinner (bool)(optional): Update spinner
                auto_reset (bool)(optional): Auto reset spinner
        """

        if self.spinner and update_spinner :
            self.spinner.update(auto_reset=auto_reset)

        if percent > 100:
            percent = 100

        self.percent = percent


    def render(
            self,
            *,
            color : int | tuple[int, int, int] = Color.C_RESET,
            hide_spinner_at_end: bool = True,
            delete : bool = False
        ) -> str:
        """
            Convert ProgressBar object to string.

            Parameters:
                color (int | tuple[int, int, int])(optional): Color
                hide_spinner_at_end (bool): Hide spinner at end
                delete (bool)(optional): Delete previous line and right on it

            Returns:
                str: ProgressBar string
        """

        from Console.ANSI.line import Line
        from Console.ANSI.color import Color

        string : str = ""

        if delete:
            string += str(Line.clear_previous_line())

        if type(color) in [int]:
            color : tuple[int, int, int] = (color, color, color)

        string += str(Color.color(color[0])) + self.__str__(color=color, hide_spinner=(hide_spinner_at_end and self.percent == 100)) + str(Color.color(Color.C_RESET))

        return string
