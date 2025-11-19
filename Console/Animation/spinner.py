#############################
###                       ###
###      Console v2.0     ###
### ----ProgressBar.py----###
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


    from Console.Animation.animation import Animation


    @staticmethod
    def stick(
        ) -> Animation:
        """
            Stick spinner.

            Returns:
                Animation: Stick animation.
        """

        from Console.Animation.animation import Animation

        return Animation(
            [
                f"[-]",
                f"[\\]",
                f"[|]",
                f"[/]"
            ]
        )


    @staticmethod
    def plus(
        ) -> Animation:
        """
            Plus spinner.

            Returns:
                Animation: Plus animation.
        """

        from Console.Animation.animation import Animation

        return Animation(
            [
                f"[-]",
                f"[|]"
            ]
        )


    @staticmethod
    def cross(
        ) -> Animation:
        """
            Cross spinner.

            Returns:
                Animation: Cross animation.
        """

        from Console.Animation.animation import Animation

        return Animation(
            [
                f"[/]",
                f"[\\]"
            ]
        )
