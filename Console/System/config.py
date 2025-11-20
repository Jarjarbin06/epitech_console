#############################
###                       ###
###      Console v2.0     ###
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
            path : str,
        ) -> bool:
        """
            Check if config.ini is empty

            Returns:
                bool: True if empty, False otherwise
        """

        empty_config : bool = False

        with open(path, 'r') as config_file:
            if config_file.read() == "":
                empty_config = True

        config_file.close()

        return empty_config