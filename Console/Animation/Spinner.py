#############################
###                       ###
###      Console v2.0     ###
### ----ProgressBar.py----###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


class Spinner:
    """
        ProgressBar class.

        Progress-bar tool.
    """


    try:
        from Console.Animation import Animation
    except Exception:
        raise ImportError('Animation failed to import in Spinner.py')


    @staticmethod
    def stick(
        ) -> Animation:
        """
        """

        try:
            from Console.Animation import Animation
        except Exception:
            raise ImportError('Animation failed to import in Spinner.py')

        return Animation(["[-]", "[\\]", "[|]", "[/]"])


    @staticmethod
    def plus(
    ) -> Animation:
        """
        """

        try:
            from Console.Animation import Animation
        except Exception:
            raise ImportError('Animation failed to import in Spinner.py')

        return Animation(["[-]", "[|]"])


    @staticmethod
    def cross(
    ) -> Animation:
        """
        """

        try:
            from Console.Animation import Animation
        except Exception:
            raise ImportError('Animation failed to import in Spinner.py')

        return Animation(["[/]", "[\\]"])
