#############################
###                       ###
###      Console v2.0     ###
###    ----test.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

if __name__ == '__main__':

    from Console import ANSI, Error

    epitech_color : ANSI.ANSI = ANSI.Color.rgb_fg(0, 145, 211)
    reset : ANSI.ANSI = ANSI.ANSI(ANSI.Color.C_RESET)
    #text : Text = epitech_color + ANSI.clear() + ANSI.right(10) + "--==## EPITECH ##==--" + reset
    print(epitech_color + ANSI.Line.clear() + ANSI.Cursor.down(1) + ANSI.Cursor.right(10) + "--==## EPITECH ##==--" + reset)
    print(Error.Error("test", link=(__file__, 5)))
