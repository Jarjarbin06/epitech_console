#############################
###                       ###
###      Console v2.0     ###
###    ----test.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################

if __name__ == '__main__':

    from Console import *

    epitech_color : ANSI.ANSI = ANSI.Color.rgb_fg(0, 145, 211)
    reset : ANSI.ANSI = ANSI.ANSI(ANSI.Color.C_RESET)

    anim = Animation.Spinner.stick()
    print(ANSI.Cursor.hide())
    watch = System.StopWatch()
    watch.start()
    for _ in range(20):
        anim.update(auto_reset=True)
        watch.update()
        print(epitech_color + anim.render(delete=True) + reset + watch)
        watch.reset()
        System.Time.sleep(0.2)
    watch.stop()
    print(ANSI.Cursor.show(), end="")
