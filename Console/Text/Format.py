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
        raise ImportError('Text failed to import in Format.py')
