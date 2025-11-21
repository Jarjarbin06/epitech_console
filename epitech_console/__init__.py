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


def _init() -> None:
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
            banner_size = 50

            epitech = Color.epitech_fg()
            epitech_dark = Color.epitech_dark_fg()
            reset = Color.color(Color.C_RESET)

            offset_t = T("  ")
            title_t = epitech + T(f"{config.get("PACKAGE", "name")}").bold().underline() + reset + "  " + T.url_link("https://github.com/Jarjarbin06/epitech_console", text="repository")
            version_t = Cursor.move_column(banner_size - 14) + epitech_dark + T("version ").italic() + T(f"{config.get("PACKAGE", "version")}").bold() + reset
            desc_t = T("Text • Animations • ANSI • Error • System").italic()
            line_t = epitech + ("─" * banner_size) + reset

            Console.print(line_t)
            Console.print(offset_t + title_t + " " + version_t + offset_t)
            Console.print(offset_t + desc_t + offset_t)
            Console.print(line_t)

        except ModuleNotFoundError:
            print("epitech_console imported (repo : https://github.com/Jarjarbin06/epitech_console)")


_init()
