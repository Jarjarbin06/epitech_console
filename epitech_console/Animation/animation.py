#############################
###                       ###
###    Epitech Console    ###
###  ----animation.py---- ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any
from epitech_console.Text.format import Format
from epitech_console.System.setting import Setting
Setting.update()


if Setting.S_SETTING_LOG: Setting.S_LOG.log("INFO", "init", "Animation.Animation: imported")


class Animation(Format):
    """
        Animation class.

        Animation tool.
    """


    from epitech_console.ANSI.color import Color


    def __init__(
            self,
            animation : list[Any] | str = ""
        ) -> None:
        """
            Create an animation.

            Parameters:
                animation (list[str] | str, optional): list of step
        """

        from epitech_console.Error.error import ErrorType

        if not isinstance(animation, (list, str)):
            if Setting.S_SETTING_LOG: Setting.S_LOG.log("ERROR", "type", f"Animation.Animation.__init__: animation is of an unsupported type (supported: list[Any], str ; current: {type(animation)})")
            raise ErrorType()

        self.animation : list[str] = []

        if isinstance(animation, list):
            for step in animation:
                self.animation.append(str(step))

        else:
            self.animation = animation.split("\\")

        self.length : int = len(self.animation)
        self.step : int = 0


    def __add__(
            self,
            other : Any | str
        ) -> Any:
        """
            Add 2 Animations together.

            Parameters:
                other (Animation | ANSI | Text | StopWatch | str): Animation

            Returns:
                Animation: Animation
        """

        from epitech_console.Error.error import ErrorType
        from epitech_console.Text.text import Text
        from epitech_console.ANSI.ansi import ANSI
        from epitech_console.System.stopwatch import StopWatch

        if not isinstance(other, (Animation, ANSI, Text, StopWatch, str)):
            if Setting.S_SETTING_LOG: Setting.S_LOG.log("ERROR", "type", f"Animation.Animation.__add__: other is of an unsupported type (supported: Animation, ANSI, Text, StopWatch, str ; current: {type(other)})")
            raise ErrorType()

        if type(other) in [Animation]:
            return Animation(self.animation + other.animation)

        elif type(other) in [Text, StopWatch, ANSI, str]:
            return Animation(self.animation + [str(other)])

        else:
            return Animation([])


    def __getitem__(
            self,
            item : int
        ) -> str :
        """
            Get the current step of the animation and convert it to a string.

            Returns:
                str: Animation string
        """

        from epitech_console.Error.error import ErrorType

        if not isinstance(item, int):
            if Setting.S_SETTING_LOG: Setting.S_LOG.log("ERROR", "type", f"Animation.Animation.__getitem__: item is of an unsupported type (supported: int ; current: {type(item)})")
            raise ErrorType()

        if self.is_last():
            return str(self.animation[self.length - 1])

        return str(self.animation[item])


    def __str__(
            self,
            *,
            color : Any = Color.color(Color.C_RESET)
        ) -> str :
        """
            Convert Animation object to string.

            Parameters:
                color (ANSI, optional): Color

            Returns:
                str: Animation string
        """

        from epitech_console.ANSI.ansi import ANSI
        from epitech_console.ANSI.color import Color

        if not isinstance(color, ANSI):
            if Setting.S_SETTING_LOG: Setting.S_LOG.log("WARN", "type", f"Animation.Animation.__str__: color is of an unsupported type (supported: ANSI ; current: {type(color)})")

        return f"{color}{str(self[self.step])}{Color.color(Color.C_RESET)}"


    def __call__(
            self,
        ) -> None:
        """
            Do a step of the animation.
        """

        self.update(auto_reset=True)


    def __len__(
            self
        ) -> int:
        """
            Return the number of steps of the animation.

            Returns:
                int: Number of steps
        """

        return self.length


    def update(
            self,
            *,
            auto_reset: bool = True
        ) -> None:
        """
            Add a step to the animation.

            Parameters:
                auto_reset (bool, optional): Automatically reset the animation. Defaults to False.
        """

        if not isinstance(auto_reset, bool):
            if Setting.S_SETTING_LOG: Setting.S_LOG.log("WARN", "type", f"Animation.Animation.update: auto_reset is of an unsupported type (supported: bool ; current: {type(auto_reset)})")

        self.step += 1

        if self.is_last() and auto_reset:
            self.reset()


    def render(
            self,
            *,
            delete : bool = False
        ) -> str:
        """
            Convert Animation object to string.

            Parameters:
                delete (bool, optional): Delete the previous animation. Defaults to False.

            Returns:
                str: Animation string
        """

        from epitech_console.ANSI.line import Line

        if not isinstance(delete, bool):
            if Setting.S_SETTING_LOG: Setting.S_LOG.log("WARN", "type", f"Animation.Animation.render: delete is of an unsupported type (supported: bool ; current: {type(delete)})")

        string : str = ""

        if delete:
            string += str(Line.clear_previous_line())

        string += str(self)

        return string


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


    def __repr__(
            self
        ) -> str:
        """
            Convert Animation object to string.

            Returns:
                str: Animation string
        """

        return f"Animation(\"{self.animation}\")"


if Setting.S_SETTING_LOG: Setting.S_LOG.log("INFO", "init", "Animation.Animation: created")
