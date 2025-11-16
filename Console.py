#############################
###                       ###
###      Console v1.0     ###
###   ----Console.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from Color import Color
from Packed import Packed
from os import system
from sys import stdout, platform
from time import sleep as slp

BASE_PACK = Packed()


class Animation:
    """
        Animation class.

        Attributes:
            ANIMATION (list[str]): list of all steps of the animation.
            ANIMATION_STEP (int): current step of the animation.
            ANIMATION_LENGTH (int): last step of the animation.
    """


    def __init__(
            self,
            animation: list[str]
        ) -> None:
        """
            Open an animation.

            Args:
                animation (list[str]): list of all steps of the animation.
        """

        self.ANIMATION : list[str] = animation
        self.ANIMATION_STEP : int = 0
        self.ANIMATION_LENGTH : int = len(animation) - 1


    def __call__(
            self,
            color_val: tuple[str, str] = BASE_PACK.VALID
        ) -> str:
        """
            Go to the next step of the animation and return it.

            Args:
                color_val (tuple[str, str])(optional): color value.
        """

        if self.ANIMATION_STEP > self.ANIMATION_LENGTH:
            self.ANIMATION_STEP -= 1

        self.ANIMATION_STEP += 1

        return color(self.ANIMATION[self.ANIMATION_STEP - 1], color_code = color_val)

    def __getitem__(
            self,
            item: int
        ) -> str:
        """
            Return the animation at step 'item'.

            Args:
                item (int): step of the animation.
        """

        return self.ANIMATION[item]


    def is_last(
            self
        ) -> bool:
        """
            Return True if the current step of the animation is the last, False otherwise.

            Returns:
                bool: True if the current step is the last, False otherwise.
        """

        return self.ANIMATION_STEP == self.ANIMATION_LENGTH


    def reset(
            self
        ) -> None:
        """
            Reset the animation back to first step.
        """

        self.ANIMATION_STEP = 0


class Action:
    """
        Action class.
    """

    @staticmethod
    def command(
            command_line: str
        ) -> None:
        """
            Execute a command in the shell.

            Args:
                command_line (str): command to execute.
        """

        system(command_line)


    @staticmethod
    def clear(
        ) -> None:
        """
            clear the console
        """

        if platform == "linux" or platform == "linux2":
            system("clear")

        elif platform == "win32":
            system("cls")


    @staticmethod
    def delete_last_line(
        ) -> None:
        """
            delete the last line of the console
        """

        stdout.write('\x1b[1A')
        stdout.write('\x1b[2K')


    @staticmethod
    def line_up(
            repeat : int = 1
        ) -> None :
        """
            bring next print to the previous line
        """

        stdout.write(f'\033[{repeat}A')


def show(
        text: str,
        *,
        start: str = "",
        end: str = "\n",
        delete: bool = False,
        sleep: int | float = 0
    ) -> None:
    """
        Show a text on the console.

        Args:
            text (str): text to show.

            start (str)(optional): starting character
            end (str)(optional): ending character
            delete (bool)(optional): delete last line
            sleep (int)(optional): sleep time
    """

    if delete: Action.delete_last_line()

    print(f"{start}{text}", end=end)
    slp(sleep)


def color(
        text: str,

        *,
        color_code: tuple[str, str] = BASE_PACK.INFO,
        title: str = "",
        indicator: str = ""
    ) -> str:
    """
        Put color on a text and return it.

        Args:
            text (str): text to show.

            color_code (tuple[str, str])(optional): color code.
            title (str)(optional): title of the text.
            indicator (str)(optional): character to indicate the color.

        Returns:
            str: colored text.
    """

    string : str = ""

    if indicator != "": string += f"{color_code[0]}{indicator}{Color.BASE} "

    if title != "": string += f"{color_code[0]}{title}{Color.BASE}{color_code[1]} : "

    string += f"{color_code[1]}{text}{Color.BASE}"

    return string


if __name__ == "__main__":

    show(color("Test started", color_code=BASE_PACK.WARNING, indicator=" "), end="\n\n\n")

    try:

        pass

    except KeyboardInterrupt:
        show(color("Test stopped", color_code=BASE_PACK.WARNING, indicator=" "), start="\n", delete=True)
