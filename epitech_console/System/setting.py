#############################
###                       ###
###    Epitech Console    ###
###   ----setting.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any


class Setting:
    """
        Setting class.

        All module's settings imported.

        Attributes:
            S_PACKAGE_NAME (str): package name.
            S_PACKAGE_VERSION (str): package version.
            S_PACKAGE_DESCRIPTION (str): package description.
            S_PACKAGE_REPOSITORY (str): package repository url.

            S_SETTING_SHOW_BANNER (str): show banner.
            S_SETTING_AUTO_COLOR (str): auto color.
            S_SETTING_SAFE_MODE (str): safe mode.
            S_SETTING_MINIMAL_MODE (str): minimal mode.
            S_SETTING_DEBUG (str): debug mode.
            S_SETTING_LOG (str): log mode.

            S_LOG (Log | None): log file.
    """


    from epitech_console.System.log import Log
    from epitech_console.System.config import Config

    S_CONFIG : Config | None = None

    S_PACKAGE_PATH : str = "null"
    S_PACKAGE_NAME : str = "null"
    S_PACKAGE_VERSION : str = "null"
    S_PACKAGE_DESCRIPTION : str = "null"
    S_PACKAGE_REPOSITORY : str = "null"

    S_SETTING_SHOW_BANNER : bool = False
    S_SETTING_AUTO_COLOR : bool = False
    S_SETTING_SAFE_MODE : bool = True
    S_SETTING_MINIMAL_MODE : bool = True
    S_SETTING_DEBUG : bool = False
    S_SETTING_LOG : bool = False
    S_SETTING_OPENED_LOG : str = "null"

    S_LOG : Log | None = None


    @staticmethod
    def update(
        ) -> None:
        """
            Initialize the BasePack class
        """

        from epitech_console.System.config import Config
        from epitech_console.System.log import Log

        Setting.S_PACKAGE_PATH = __file__.removesuffix("System/setting.py")

        Setting.S_CONFIG = Config(Setting.S_PACKAGE_PATH)

        Setting.S_PACKAGE_NAME = Setting.S_CONFIG.get("PACKAGE", "name")
        Setting.S_PACKAGE_VERSION = Setting.S_CONFIG.get("PACKAGE", "version")
        Setting.S_PACKAGE_DESCRIPTION = Setting.S_CONFIG.get("PACKAGE", "description")
        Setting.S_PACKAGE_REPOSITORY = Setting.S_CONFIG.get("PACKAGE", "repository")

        Setting.S_SETTING_SHOW_BANNER = Setting.S_CONFIG.get_bool("SETTING", "show-banner")
        Setting.S_SETTING_AUTO_COLOR = Setting.S_CONFIG.get_bool("SETTING", "auto-color")
        Setting.S_SETTING_SAFE_MODE = Setting.S_CONFIG.get_bool("SETTING", "safe-mode")
        Setting.S_SETTING_MINIMAL_MODE = Setting.S_CONFIG.get_bool("SETTING", "minimal-mode")
        Setting.S_SETTING_DEBUG = Setting.S_CONFIG.get_bool("SETTING", "debug")
        Setting.S_SETTING_LOG = Setting.S_CONFIG.get_bool("SETTING", "log")

        if Setting.S_SETTING_LOG:

            Setting.S_SETTING_OPENED_LOG = Setting.S_CONFIG.get("SETTING", "opened-log")

            if Setting.S_SETTING_OPENED_LOG == "null":
                Setting.S_LOG = Log(Setting.S_PACKAGE_PATH + "log")
                Setting.S_CONFIG.set("SETTING", "opened-log", Setting.S_LOG.log_file_name)
                Setting.S_SETTING_OPENED_LOG = Setting.S_CONFIG.get("SETTING", "opened-log")

            else:
                Setting.S_LOG = Log(Setting.S_PACKAGE_PATH + "log", file_name=Setting.S_SETTING_OPENED_LOG)

            Setting.S_LOG.log("INFO", "function", "System.Setting.update(): setting updated")
