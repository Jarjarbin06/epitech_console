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

        ProgressBar tool.
    """


    try:
        from Console.Text import Animation
    except Exception:
        raise ImportError('Animation failed to import in PrograssBar.py')
