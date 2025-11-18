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
        from Console.Text import Text
    except Exception:
        raise ImportError('Text sub-modules failed to import')
