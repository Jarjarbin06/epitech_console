#############################
###                       ###
###    Epitech Console    ###
###   ----spinner.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object


class Spinner(object):
    """
        ProgressBar class.

        Progress-bar tool.
    """


    from epitech_console.Animation.animation import Animation
    from epitech_console.Animation.style import Style


    @staticmethod
    def stick(
            *,
            style : object = Style("#", " ", "#", "#", "", "")
        ) -> Animation:
        """
            Stick spinner.

            Returns:
                Animation: Stick animation.
        """

        from epitech_console.Animation.animation import Animation

        return Animation(
            [
                f"{style.border_left}-{style.border_right}",
                f"{style.border_left}\\{style.border_right}",
                f"{style.border_left}|{style.border_right}",
                f"{style.border_left}/{style.border_right}"
            ]
        )


    @staticmethod
    def plus(
            *,
            style : object = Style("#", " ", "#", "#", "", "")
        ) -> Animation:
        """
            Plus spinner.

            Returns:
                Animation: Plus animation.
        """

        from epitech_console.Animation.animation import Animation

        return Animation(
            [
                f"{style.border_left}-{style.border_right}",
                f"{style.border_left}|{style.border_right}"
            ]
        )


    @staticmethod
    def cross(
            *,
            style : object = Style("#", " ", "#", "#", "", "")
        ) -> Animation:
        """
            Cross spinner.

            Returns:
                Animation: Cross animation.
        """

        from epitech_console.Animation.animation import Animation

        return Animation(
            [
                f"{style.border_left}/{style.border_right}",
                f"{style.border_left}\\{style.border_right}"
            ]
        )
