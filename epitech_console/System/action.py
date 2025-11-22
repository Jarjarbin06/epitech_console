#############################
###                       ###
###    Epitech Console    ###
###   ----action.py----   ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from builtins import object
from typing import Any


class Action:
    """
        Action class.

        Action object to save a function and its arguments and call it later.
    """


    from collections.abc import Callable


    def __init__(
            self,
            name : str,
            function : Callable,
            *args : Any,
            **kwargs : Any
        ) -> None:
        """
            Save a function and its arguments.

            Parameters:
                name (str): Name of the call.
                function (Callable): Function to be saved.
                *args (Any): Function's args.
                **kwargs (Any): Function's kwargs.
        """

        from collections.abc import Callable

        self.name = name
        self.functions : Callable = function
        self.args : list = list(args)
        self.kwargs : dict = dict(kwargs)


    def __call__(
            self
        ) -> Any:
        """
            Call the saved function with its arguments.

        Returns:
            Any: Return of the function's call.
        """

        return self.functions(*self.args, **self.kwargs)

