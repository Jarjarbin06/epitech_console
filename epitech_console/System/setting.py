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
    """

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


    @staticmethod
    def update(
        ) -> None:
        """
            Initialise the BasePack class
        """

        from epitech_console.System.config import Config
        from epitech_console import PATH


        config = Config(PATH)

        Setting.S_PACKAGE_NAME = config.get("PACKAGE", "name", str)
        Setting.S_PACKAGE_VERSION = config.get("PACKAGE", "version", str)
        Setting.S_PACKAGE_DESCRIPTION = config.get("PACKAGE", "description", str)
        Setting.S_PACKAGE_REPOSITORY = config.get("PACKAGE", "repository", str)

        Setting.S_SETTING_SHOW_BANNER = config.get("SETTING", "show-banner", bool)
        Setting.S_SETTING_AUTO_COLOR = config.get("SETTING", "auto-color", bool)
        Setting.S_SETTING_SAFE_MODE = config.get("SETTING", "safe-mode", bool)
        Setting.S_SETTING_MINIMAL_MODE = config.get("SETTING", "minimal-mode", bool)
        Setting.S_SETTING_DEBUG = config.get("SETTING", "debug", bool)
        Setting.S_SETTING_LOG = config.get("SETTING", "log", bool)
