#############################
###                       ###
###    Epitech Console    ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from epitech_console import Animation, ANSI, Error, System, Text
from epitech_console.System import Actions
from epitech_console.Text import Format

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


def _banner(
        config
    ) -> None:
    """
        Show a simple banner.
    """
    from epitech_console.ANSI import Color, Cursor
    from epitech_console.Text import Text as T
    from epitech_console.System import Console, Config

    banner_size = 50

    epitech = Color.epitech_fg()
    epitech_dark = Color.epitech_dark_fg()
    reset = Color.color(Color.C_RESET)

    offset_t = T("  ")
    title_t = epitech + T(f"{config.get("PACKAGE", "name")}").bold().underline() + reset + "  " + T.url_link(
        "https://github.com/Jarjarbin06/epitech_console", text="repository")
    version_t = T(" " * 5) + epitech_dark + T("version ").italic() + T(
        f"{config.get("PACKAGE", "version")}").bold() + reset
    desc_t = T("   Text • Animation • ANSI • Error • System   ").italic()
    line_t = epitech + ("─" * banner_size) + reset

    Console.print(line_t, offset_t + title_t + " " + version_t + offset_t, offset_t + desc_t + offset_t, line_t, separator="\n")


def _init(
    ) -> None:
    """
        _init() initializes the epitech console package and show a banner (if SETTING : show-banner = True in config.ini)
    """
    from epitech_console.ANSI import Color, Cursor
    from epitech_console.Text import Text as T
    from epitech_console.System import Console, Config, Action

    if not Config.exist(PATH):
        Config.create(PATH)

    config = Config.read(PATH)

    if config.getboolean("SETTING", "show-banner"):
        try:
            _banner(config)

        except Exception as error:
            if config.getboolean("SETTING", "debug"):
                print("\033[101m \033[0m \033[91m" + str(error) + "\033[0m\n")
            print(
                "\033[103m \033[0m \033[93mepitech_console imported with error\033[0m\n"
                "\033[103m \033[0m\n"
                "\033[103m \033[0m \033[93mPlease reinstall with :\033[0m\n"
                "\033[103m \033[0m \033[93m    'pip install --upgrade --force-reinstall epitech_console'\033[0m\n"
                "\033[103m \033[0m\n"
                "\033[103m \033[0m \033[93mPlease report the issue here : https://github.com/Jarjarbin06/epitech_console/issues\033[0m\n"
            )


_init()
