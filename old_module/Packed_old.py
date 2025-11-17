#############################
###                       ###
###      Console v1.0     ###
###   ----Packed.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from Color_old import Color

class Packed:
    """
        Packed class.
        Base animation pack ready for use.

        Attributes:
            ERROR (tuple): error tuple of color.
            WARNING (tuple): warning tuple of color.
            VALID (tuple): validation tuple of color.
            INFO (tuple): information tuple of color.
            SLIDE_R (tuple): slide right animation.
            SLIDE_L (tuple): slide left animation.
            SLIDER_R (tuple): slider right animation.
            SLIDER_L (tuple): slider left animation.
            FILL_R (tuple): fill right animation.
            FILL_L (tuple): fill left animation.
            EMPTY_R (tuple): empty right animation.
            EMPTY_L (tuple): empty left animation.
            FULL (tuple): full animation.
            EMPTY (tuple): empty animation.
    """

    def __init__(
            self,

            *,
            on : str = "#",
            off : str = "-",
            arrow_right : str | None = None,
            arrow_left : str | None = None,
            borders : tuple[str, str] = ("|", "|")
        ) -> None:
        """
            Initialise the Packed class

            Parameters:
                on (str)(optional): character representing an activated case
                off (str)(optional): character representing an unactivated case
                arrow_right (str | None)(optional): character representing the right of activated cases
                arrow_left (str | None)(optional): character representing the right of activated cases
                borders (tuple)(optional): character representing a border
        """

        if not arrow_right: arrow_right = on
        if not arrow_left: arrow_left = on

        self.ERROR = (Color.HIGHLIGHT_DARK_RED, Color.DARK_RED)
        self.WARNING = (Color.HIGHLIGHT_DARK_YELLOW, Color.DARK_YELLOW)
        self.VALID = (Color.HIGHLIGHT_DARK_GREEN, Color.DARK_GREEN)
        self.INFO = (Color.HIGHLIGHT, Color.BASE)

        self.SLIDE_R = [
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{borders[1]}"]

        self.SLIDE_L = [
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}"]

        self.SLIDER_R = [
            f"{borders[0]}{arrow_left}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{borders[1]}"]

        self.SLIDER_L = [
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{arrow_right}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{arrow_left}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}"]

        self.FILL_R = [
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{on}{on}{on}{arrow_right}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{arrow_right}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{arrow_right}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{arrow_right}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{arrow_right}{borders[1]}"]

        self.FILL_L = [
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{on}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{arrow_left}{on}{on}{on}{on}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{arrow_left}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{arrow_left}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{arrow_left}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{arrow_left}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{borders[1]}"]

        self.EMPTY_R = [
            f"{borders[0]}{arrow_left}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{arrow_left}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{arrow_left}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{arrow_left}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{arrow_left}{on}{on}{on}{on}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{on}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{on}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{arrow_left}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}"]

        self.EMPTY_L = [
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{arrow_right}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{arrow_right}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{arrow_right}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{arrow_right}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{on}{on}{on}{arrow_right}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{on}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{arrow_right}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}",
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}"]

        self.FULL = [
            f"{borders[0]}{arrow_left}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{on}{arrow_right}{borders[1]}"]

        self.EMPTY = [
            f"{borders[0]}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{off}{borders[1]}"]
