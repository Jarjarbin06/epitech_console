#############################
###                       ###
###    Epitech Console    ###
###     ----TUI.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any


from epitech_console.System.setting import Setting


Setting.update()


if Setting.S_SETTING_LOG_MODE: Setting.S_LOG_FILE.log("INFO", "init", "Text.Format: imported")


class TUI:
    pass
