#############################
###                       ###
###    Epitech Console    ###
###     ----Line.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


class Config:
    """
    """


    @staticmethod
    def is_empty(
            path : str
        ) -> bool:
        """
            Check if a config file config.ini is empty

            Returns:
                bool: True if empty, False otherwise
        """

        empty_config : bool = False

        try :
            with open(path + "config.ini", 'r') as config_file:
                if config_file.read() == "":
                    empty_config = True

        except FileNotFoundError:
            empty_config = True

        config_file.close()

        return empty_config

    @staticmethod
    def create(
            path : str,
            data : dict | None = None
        ) -> None:
        """
            Create a new config file

            Parameters:
                path (str): path to folder which you want you config file to be in
                data (dict | None): data to put in the config file
        """

        from configparser import ConfigParser

        if not data :
            data = {
                "GENERAL" : {
                    "version" : "0.0.0",
                    "debug": "False",
                    "log": "True",
                    "introduction": "True"
                }
            }

        with open(path + "config.ini", 'w') as config_file:
            config = ConfigParser()
            for key in data:
                config[key] = data[key]

            config.write(config_file)

        config_file.close()