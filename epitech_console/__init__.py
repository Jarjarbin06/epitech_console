#############################
###                       ###
###    Epitech Console    ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any


from epitech_console import Animation, ANSI, Error, System, Text
from epitech_console.System import Actions
from epitech_console.Text import Format


__version__ : str = 'v0.1.8'
__author__ : str = 'Nathan Jarjarbin'
__email__ : str = 'nathan.amaraggi@epitech.eu'


def _banner(
    ) -> None:
    """
        Show a simple banner.
    """

    banner_size = 50

    epitech = ANSI.Color.epitech_fg()
    epitech_dark = ANSI.Color.epitech_dark_fg()
    reset = ANSI.Color.color(ANSI.Color.C_RESET)

    offset_t = Text.Text("  ")
    title_t = epitech + Text.Text(f'{System.Setting.S_PACKAGE_NAME}').bold().underline() + reset + "  " + Text.Text.url_link(
        "https://github.com/Jarjarbin06/epitech_console", text="repository")
    version_t = Text.Text(" " * 5) + epitech_dark + Text.Text("version ").italic() + Text.Text(
        f'{System.Setting.S_PACKAGE_VERSION}').bold() + reset
    desc_t = Text.Text("   Text • Animation • ANSI • Error • System   ").italic()
    line_t = epitech + ("─" * banner_size) + reset

    System.Console.print(line_t, offset_t + title_t + " " + version_t + offset_t, offset_t + desc_t + offset_t, line_t, separator="\n")


def init(
    ) -> None:
    """
        init() initializes the epitech console package and show a banner (if SETTING : show-banner = True in config.ini)
    """

    try:
        System.Setting.update()
        Animation.BasePack.update()
        ANSI.BasePack.update()

        if System.Setting.S_SETTING_SHOW_BANNER:
            _banner()

    except Error.Error as error:
        print(error)
        print(Error.Error._lauch_message())

    except Exception as error:
        print(f"\033[101m \033[0m \033[91m{error}\033[0m")
        print(
            "\033[103m \033[0m \033[93mepitech_console launched with error\033[0m\n"
            "\033[103m \033[0m\n"
            "\033[103m \033[0m \033[93mPlease reinstall with :\033[0m\n"
            "\033[103m \033[0m \033[93m    'pip install --upgrade --force-reinstall epitech_console'\033[0m\n"
            "\033[103m \033[0m\n"
            "\033[103m \033[0m \033[93mPlease report the issue here : https://github.com/Jarjarbin06/epitech_console/issues\033[0m\n"
        )


def quit(
        *,
        show : bool = False,
        delete_log: bool = False
    ) -> None:
    """
        quit() uninitializes the epitech console package

        Parameters:
            show (bool, optional) : show the log file on terminal
            delete_log (bool, optional) : delete the log file
    """

    if System.Setting.S_SETTING_LOG:
        System.Setting.S_LOG.close()
        System.Setting.S_CONFIG.set("SETTING", "opened-log", "null")

        if show:
            System.Setting.S_LOG.show()

        if delete_log:
            System.Setting.S_LOG.close(True)


__all__ : list[str] = [
    'Animation',
    'ANSI',
    'Error',
    'System',
    'Text',
    'init',
    'quit',
    '__version__',
    '__author__',
    '__email__'
]
