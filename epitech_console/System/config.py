#############################
###                       ###
###    Epitech Console    ###
###   ----config.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object, type
from typing import Any


class Config:
    """
        Config class.

        Config file tool.
    """


    def __init__(
            self,
            path : str,
            data : dict | None = None,
            *,
            file_name : str = "config.ini"
        ) -> None:
        """
            Create a new config file if 'path'/'file_name' does not exist, read otherwise.

            Parameters:
                path (str): path to folder which you want your config file to be in
                data (dict | None, optional): data to put in the config file
                file_name (str, optional): name of config file
        """

        from configparser import ConfigParser

        if path[-1] != "/":
            path += "/"

        self.config : ConfigParser | None = ConfigParser()
        self.path : str = path
        self.file_name : str = file_name

        if Config.exist(self.path):
            self.config.read(self.path + self.file_name)

        else:
            if not data and self.file_name == "config.ini":
                data = {}
            with open(self.path + self.file_name, 'w') as config_file:
                for key in data:
                    self.config[key] = data[key]

                self.config.write(config_file)

            config_file.close()


    def get(
            self,
            section : str,
            option : str,
            wanted_type : type = str
        ) -> Any:
        """
            Get a value from the config file.

            Parameters:
                section (str): section name
                option (str): option name
                wanted_type (type, optional): type to check

            Returns:
                Any
        """

        return wanted_type(self.config.get(section, option))


    def delete(
            self,
            cached : bool = False
        ) -> bool:
        """
            Delete the config file.

            Parameters:
                cached (bool, optional): keep the config file's data in memory

            Returns:
                bool: True if deleted else False
        """

        from os import remove

        if self.path[-1] != "/":
            self.path += "/"

        remove(self.path + self.file_name)

        if not cached:
            self.config = None

        return not Config.exist(self.path, file_name=self.file_name)


    @staticmethod
    def exist(
            path : str,
            *,
            file_name : str = "config.ini"
        ) -> bool:
        """
            Check if a config file config.ini is empty or doesn't exist

            Returns:
                bool: False if empty or not existing, True otherwise
                file_name (str, optional): name of config file
        """

        if path[-1] != "/":
            path += "/"

        empty_config : bool = True

        try :
            with open(path + file_name, 'r') as config_file:
                if config_file.read() == "":
                    empty_config = False
            config_file.close()

        except FileNotFoundError:
            empty_config = False

        return empty_config
