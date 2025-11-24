#############################
###                       ###
###    Epitech Console    ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from epitech_console import Animation, ANSI, Error, System, Text


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


def _simple_banner(
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
    version_t = Cursor.move_column(banner_size - 14) + epitech_dark + T("version ").italic() + T(
        f"{config.get("PACKAGE", "version")}").bold() + reset
    desc_t = T("   Text • Animation • ANSI • Error • System   ").italic()
    line_t = epitech + ("─" * banner_size) + reset

    Console.print(line_t)
    Console.print(offset_t + title_t + " " + version_t + offset_t)
    Console.print(offset_t + desc_t + offset_t)
    Console.print(line_t)
    Console.print()


def _animated_banner(
        config
    ) -> None:
    """
        Show an animation.
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
    version_t = Cursor.move_column(banner_size - 14) + epitech_dark + T("version ").italic() + T(
        f"{config.get("PACKAGE", "version")}").bold() + reset
    desc_t = T("   Text • Animation • ANSI • Error • System   ").italic()
    line_t = epitech + ("─" * banner_size) + reset

    Console.print(line_t)
    Console.print(offset_t + title_t + " " + version_t + offset_t)
    Console.print(offset_t + desc_t + offset_t)
    Console.print(line_t)
    Console.print()


def _init(
    ) -> None:
    """
        _init() initializes the epitech console package and show a banner (if SETTING : show-banner = True in config.ini)
    """
    from epitech_console.ANSI import Color, Cursor
    from epitech_console.Text import Text as T
    from epitech_console.System import Console, Config

    if not Config.exist(PATH):
        Config.create(PATH)

    config = Config.read(PATH)

    if config.getboolean("SETTING", "show-banner"):
        try:
            if config.getboolean("SETTING", "animated-banner"):
                _animated_banner(config)
            else:
                _simple_banner(config)

        except Exception:
            print(
                "epitech_console imported with error\n"
                "\n"
                "Please reinstall with :\n"
                "    'pip install --upgrade --force-reinstall epitech_console'\n"
                "\n"
                "Please report the issue here : https://github.com/Jarjarbin06/epitech_console/issues\n"
            )


_init()
