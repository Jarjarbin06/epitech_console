#############################
###                       ###
###      Console v2.0     ###
###     ----Line.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from configparser import ConfigParser


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

        with open(path + "config.ini", 'r') as config_file:
            if config_file.read() == "":
                empty_config = True

        config_file.close()

        return empty_config

    @staticmethod
    def create(
            path : str,
            data : dict | None = None
        ) -> None:
        """
        """

        if not data :
            data = {
                "GENERAL" : {
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