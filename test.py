#############################
###                       ###
###      Console v2.0     ###
###    ----test.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################
from Console.Animation import Animation

if __name__ == '__main__':

    from Console import *

    epitech_color : ANSI.ANSI = ANSI.Color.rgb_fg(0, 145, 211)
    reset : ANSI.ANSI = ANSI.ANSI(ANSI.Color.C_RESET)

    text : Text.Text = Text.Text(
        epitech_color +
        ANSI.Line.clear() +
        ANSI.Cursor.down(1) +
        ANSI.Cursor.right(10) +
        "--==##  JARJARBIN's STUDIO  ##==--" +
        reset
    )

    print(text)
    print(str(Error.Error("test", link=(__file__, 28))) + "\n\n")

    anim = Animation.Spinner.stick()
    for _ in range(20):
        anim()
        print(ANSI.Line.clear_previous_line() + anim)
        System.Time.sleep(0.2)
