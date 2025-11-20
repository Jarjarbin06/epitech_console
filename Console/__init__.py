#############################
###                       ###
###      Console v2.0     ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from Console import Animation, ANSI, Error, System, Text
from configparser import ConfigParser


PATH = __file__.removesuffix("__init__.py")


__all__ : list[str] = [
    'Animation',
    'ANSI',
    'Error',
    'System',
    'Text',
    'PATH'
]


if System.Config.is_empty(PATH + "config.ini"):

    with open(PATH + "config.ini", 'w') as config_file:
        config = ConfigParser()
        config['GENERAL'] = {
            "debug": "False",
            "log": "True",
            "introduction": "True",
        }

        config.write(config_file)
    config_file.close()

Animation.BasePack.update(Animation.Style("#", " ", "#", "#", "", ""))

epitech_color : ANSI.ANSI = ANSI.Color.rgb_bg(0, 145, 211) + ANSI.Color.color(ANSI.Color.C_WHITE)
reset : ANSI.ANSI = ANSI.Color.color(ANSI.Color.C_RESET)
anim_1 : Animation.Animation = Animation.Animation(Animation.BasePack.P_FILL_L)
anim_2 : Animation.Animation = Animation.Animation(Animation.BasePack.P_FILL_R)
text : Text.Text = Text.Text(" Console v2.0 ")
line : Text.Text = Text.Text() + anim_1.render(delete=True) + text + anim_2.render()

for _ in range(anim_1.length):
    anim_1.update()
    anim_2.update()
    line = Text.Text() + anim_1.render(delete=True) + text + anim_2.render()
    System.Console.print(line, sleep=0.1)

System.Time.sleep(2)