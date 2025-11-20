#############################
###                       ###
###    Epitech Console    ###
###   ----Format.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object, any


class Format:
    """
        Format class.

        Format tool.
    """


    def reset(
            self
        ) -> any:
        """
            Apply the 'reset' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Returns:
                any: formatted object.
        """

        from epitech_console.ANSI.color import Color

        return Format.apply(self, Color.color(Color.C_RESET))



    def bold(
            self
        ) -> any:
        """
            Apply the 'bold' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Returns:
                any: formatted object.
        """

        from epitech_console.ANSI.color import Color

        return Format.apply(self, Color.color(Color.C_BOLD))


    def italic(
            self
        ) -> any:
        """
            Apply the 'italic' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Returns:
                any: formatted object.
        """
        from epitech_console.ANSI.color import Color

        return Format.apply(self, Color.color(Color.C_ITALIC))


    def underline(
            self
        ) -> any:
        """
            Apply the 'underline' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Returns:
                any: formatted object.
        """

        from epitech_console.ANSI.color import Color

        return Format.apply(self, Color.color(Color.C_UNDERLINE))


    def hide(
            self
        ) -> any:
        """
            Apply the 'hide' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Returns:
                any: formatted object.
        """

        from epitech_console.ANSI.color import Color

        return Format.apply(self, Color.color(Color.C_HIDDEN))


    def strikethrough(
            self
        ) -> any:
        """
            Apply the 'strikethrough' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Returns:
                any: formatted object.
        """

        from epitech_console.ANSI.color import Color

        return Format.apply(self, Color.color(Color.C_STRIKETHROUGH))


    def error(
            self,
            *,
            title : bool = False
        ) -> any:
        """
            Apply the 'error' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Parameters:
                title (bool): whether it is a title or not

            Returns:
                any: formatted object.
        """

        from epitech_console.ANSI.color import Color
        from epitech_console.ANSI.basepack import BasePack

        if title:
            return Format.apply(self, Color.color(BasePack.P_ERROR[0]))
        return Format.apply(self, Color.color(BasePack.P_ERROR[1]))


    def warning(
            self,
            *,
            title : bool = False
        ) -> any:
        """
            Apply the 'warning' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Parameters:
                title (bool): whether it is a title or not

            Returns:
                any: formatted object.
        """

        from epitech_console.ANSI.color import Color
        from epitech_console.ANSI.basepack import BasePack

        if title:
            return Format.apply(self, Color.color(BasePack.P_WARNING[0]))
        return Format.apply(self, Color.color(BasePack.P_WARNING[1]))


    def ok(
            self,
            *,
            title : bool = False
        ) -> any:
        """
            Apply the 'ok' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Parameters:
                title (bool): whether it is a title or not

            Returns:
                any: formatted object.
        """

        from epitech_console.ANSI.color import Color
        from epitech_console.ANSI.basepack import BasePack

        if title:
            return Format.apply(self, Color.color(BasePack.P_OK[0]))
        return Format.apply(self, Color.color(BasePack.P_OK[1]))


    def info(
            self,
            *,
            title : bool = False
        ) -> any:
        """
            Apply the 'info' format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Parameters:
                title (bool): whether it is a title or not

            Returns:
                any: formatted object.
        """

        from epitech_console.ANSI.color import Color
        from epitech_console.ANSI.basepack import BasePack

        if title:
            return Format.apply(self, Color.color(BasePack.P_INFO[0]))
        return Format.apply(self, Color.color(BasePack.P_INFO[1]))


    @staticmethod
    def apply(
            obj : object,
            sequence : object | None = None
        ) -> any:
        """
            Apply a format to an object of type Text, ANSI, Animation, ProgressBar or str.

            Parameters:
                obj (Text | ANSI | Animation | ProgressBar | str): object to be formatted.
                sequence (ANSI): format.

            Returns:
                any: formatted object.
        """

        from epitech_console.ANSI.color import Color
        from epitech_console.Text.text import Text
        from epitech_console.ANSI.ansi import ANSI
        from epitech_console.Animation.animation import Animation
        from epitech_console.Animation.progressbar import ProgressBar

        if not sequence:
            sequence: ANSI = Color.color(Color.C_BOLD)

        if type(obj) in [str]:
            return str(sequence) + str(obj)

        if type(obj) in [Text]:
            return Text(str(sequence) + str(obj))

        if type(obj) in [ANSI]:
            return ANSI(str(sequence) + str(obj))

        if type(obj) in [Animation]:
            animation: list[str] = [(str(sequence) + str(line)) for line in obj.animation]
            return Animation(animation)

        if type(obj) in [ProgressBar]:
            animation: Animation = Animation([(str(sequence) + str(line)) for line in obj.animation])
            spinner: Animation = Animation([(str(sequence) + str(line)) for line in obj.spinner])
            return ProgressBar(obj.length, animation=animation, style=obj.style, percent_style=obj.percent_style,  spinner=spinner, spinner_position=obj.spinner_position)
