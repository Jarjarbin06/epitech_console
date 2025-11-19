#############################
###                       ###
###      Console v2.0     ###
###    ----test.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


if __name__ == '__main__':

    from Console import ANSI, Error, Text, System, Animation

    watch = System.StopWatch(True)

    epitech_color = ANSI.Color.rgb_fg(0, 145, 211)
    reset = ANSI.Color.color(ANSI.Color.C_RESET)

    spin = Animation.Spinner.stick()
    bar = Animation.ProgressBar(50, percent_style="mix", spinner=spin)

    System.Console.print(ANSI.Line.clear() + ANSI.Cursor.hide())

    for p in range(101):
        bar.update(p)
        watch.update()

        text = Text.Text(ANSI.Cursor.move_column(25) + bar.render(color=ANSI.Color.C_RED, delete=True) + ANSI.Cursor.move_column(0) + epitech_color + watch + reset)
        System.Console.print(text)

        watch.reset()
        System.Time.sleep(0.1)

    text = Text.Text(ANSI.Cursor.move_column(25) + bar.render(color=ANSI.Color.C_GREEN, delete=True) + ANSI.Cursor.move_column(0) + epitech_color + watch + reset + ANSI.Cursor.show())
    System.Console.print(text)
    watch.stop()
