#############################
###                       ###
###      Console v2.0     ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from Console.ANSI.ansi import ANSI
from Console.ANSI.cursor import Cursor
from Console.ANSI.line import Line
from Console.ANSI.color import Color
from Console.ANSI.basepack import BasePack


__all__ : list[str] = [
    'ANSI',
    'Cursor',
    'Line',
    'Color',
    'BasePack'
]


__author__ : str = 'Nathan Jarjarbin'
__email__ : str = 'nathan.epitech.eu'
