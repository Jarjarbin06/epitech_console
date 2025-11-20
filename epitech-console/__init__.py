#############################
###                       ###
###      Console v2.0     ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from Console import Animation, ANSI, Error, System, Text


PATH = __file__.removesuffix("__init__.py")


Animation.basepack.BasePack.update(Animation.Style("#", " ", "#", "#", "", ""))
ANSI.basepack.BasePack.update()


__all__ : list[str] = [
    'Animation',
    'ANSI',
    'Error',
    'System',
    'Text',
    'PATH'
]


__author__ : str = 'Nathan Jarjarbin'
__email__ : str = 'nathan.epitech.eu'


if System.config.Config.is_empty(PATH):
    System.config.Config.create(PATH)


epitech_color : ANSI.ANSI = ANSI.Color.rgb_fg(0, 145, 211) + ANSI.Color.rgb_bg(0, 0 ,0)
reset : ANSI.ANSI = ANSI.Color.color(ANSI.Color.C_RESET)
text : Text.Text = epitech_color + Text.Text("hi").bold() + reset

System.Console.print(text, sleep=2)