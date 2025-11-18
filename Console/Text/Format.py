#############################
###                       ###
###      Console v2.0     ###
###   ----Format.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


class Format:
    """
        Format class.

        Format tool.
    """


    try:
        from Console.Text import Text
    except Exception:
        raise ImportError('Text sub-modules failed to import')
