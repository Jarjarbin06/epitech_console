#############################
###                       ###
###    Epitech Console    ###
###     ----log.py----    ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any


class Log:
    """
        Log class.

        Log file tool.
    """


    def __init__(
            self,
            path : str,
            file_name : str | None = None
        ) -> None:
        """
            Log class constructor.

            Parameters:
                path (str): path to log file
                file_name (str | None, optional): name of log file
        """

        from datetime import datetime

        self.log_path : str = (path if path[-1] == "/" else path + "/")
        self.log_file_name : str = str(datetime.now()).replace(":", "_") if not file_name else file_name

        try :
            with open(f"{self.log_path}{self.log_file_name}.txt", 'r') as log_file:
                if log_file.read() == "":
                    raise FileNotFoundError
            log_file.close()

        except FileNotFoundError:
            try :
                with open(f"{self.log_path}{self.log_file_name}.txt", 'a') as log_file:
                    log_file.write("   date          time      | [type_] title    | detail\n\n---START---")
                log_file.close()
            except FileNotFoundError:
                pass


    def log(
            self,
            status : str,
            title : str,
            description : str
        ) -> None:
        """
            Format a log message then save it.

            Parameters:
                status (str): log status
                title (str): log title
                description (str): log description
        """

        from datetime import datetime

        status += "_" * (5 - len(status))
        status = status[:4]
        title += " " * (8 - len(title))
        title = title[:8]

        log_time : str = str(datetime.now())
        log_str : str = f"{log_time} | [{status}] {title} | {description}"

        self.save(log_str)


    def comment(
            self,
            comment : str
        ) -> None:
        """
            Save a comment in the log file.

            Parameters:
                comment (str): comment
        """

        self.save(f">>> {comment}")


    def save(
            self,
            log_str : str
        ) -> None:
        """
            Save a new log in the log file.

            Parameters:
                log_str (str): log string
        """

        try :
            with open(f"{self.log_path}{self.log_file_name}.txt", 'a') as log_file :
                log_file.write(f"\n{log_str}")
            log_file.close()
        except FileNotFoundError:
            pass


    def close(
            self,
            delete_logs : bool = False
        ) -> None :
        """
            Close the log file.

            Parameters:
                delete_logs (bool, optional): delete the log file
        """

        from os import remove

        try:
            with open(f"{self.log_path}{self.log_file_name}.txt", 'a') as log_file :
                log_file.write(f"\n----END----\n")
            log_file.close()
        except FileNotFoundError:
            pass

        if delete_logs :
            try :
                remove(f"{self.log_path}{self.log_file_name}.txt")
            except FileNotFoundError:
                pass


    def read(
            self
        ) -> str :
        """
            Read the log file and returns its content.

            Returns:
                str: content of the log file
        """

        log_str : str

        try:
            with open(f"{self.log_path}{self.log_file_name}.txt", 'r') as log_file:
                log_str = log_file.read()
            log_file.close()
        except FileNotFoundError:
            pass

        return log_str


    def show(
            self
        ) -> None :
        """
            Show a formated log file.
        """

        from epitech_console.System import Console
        from epitech_console.ANSI import BasePack, Color

        log_str = self.read()

        color_dict: dict = {
            "[INFO_]" : BasePack.P_INFO,
            "[VALID]" : BasePack.P_VALID,
            "[WARN_]" : BasePack.P_WARNING,
            "[ERROR]" : BasePack.P_ERROR,
        }
        c_reset : Any = Color.color(Color.C_RESET)
        c_under : Any = Color.color(Color.C_UNDERLINE)
        c_bold : Any = Color.color(Color.C_BOLD)
        start : int = log_str.index("---START---\n") + len("---START---\n")
        end : int = log_str.index("----END----\n")
        logs : list = [lines.split(" | ") for lines in log_str[start:end].splitlines()]
        t_size = len(Console)
        footer : str = f"{c_under}{BasePack.P_INFO[0]}|{c_reset}{c_bold}{c_under}"
        detail_size : int
        string : str = ""

        string += f"{c_under}{BasePack.P_INFO[0]}|{c_reset}{c_bold}{c_under}    date          time      | {c_reset}{c_under}{BasePack.P_INFO[0]}[type_]{c_reset}{c_bold}{c_under} category | detail" + (" " * (t_size - 56)) + f"{c_reset}\n"
        string += f"{BasePack.P_INFO[0]}|{c_reset}{c_bold}" + (" " * (t_size - 1)) + f"{c_reset}\n"

        for log_line in logs :
            if log_line[0][:3] == ">>>" :
                string += f"{BasePack.P_INFO[0]}>>>{c_reset} {BasePack.P_INFO[1]}{log_line[0][3:]}{c_reset}\n"

            else :
                if len(log_line) == 3 and log_line[1][:7].upper() in color_dict :
                    color = color_dict[log_line[1][:7].upper()]
                    string += (
                        f"{color[0]}|{c_reset} " +
                        f"{color[1]}{log_line[0]}{c_reset} | " +
                        f"{color[0]}{log_line[1][0:7]}{c_reset} " +
                        f"{color[1]}{log_line[1][8:]}{c_reset} | " +
                        (f"{log_line[2][:(t_size - 1)]}..." if len(log_line[2]) > (t_size - 1) else f"{color[1]}{log_line[2]}") +
                        f"{c_reset}\n")
                elif len(log_line) == 1:
                    string += f"{Color.color(Color.C_BG_DARK_CYAN)}|{c_reset} " + f"{Color.color(Color.C_FG_DARK_CYAN)}UNFORMATTED\n\"{log_line[0]}\"{c_reset}\n"

        string += footer + (" " * (t_size - 1)) + f"{c_reset}\n"

        Console.print(string)


    def __repr__(
            self
        ) -> str:
        """
            Convert Log object to string.

            Returns:
                str: Log string
        """

        return f"Log(\"{self.log_path}\", \"{self.log_file_name}\")"
