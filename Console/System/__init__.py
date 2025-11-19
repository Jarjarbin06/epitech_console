#############################
###                       ###
###      Console v2.0     ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from Console.System.time import Time
from Console.System.stopwatch import StopWatch
from Console.System.console import Console

from sys import stdin, stdout, stderr


__all__ : list[str] = [
    'Time',
    'StopWatch',
    'Console',
    'stdin',
    'stdout',
    'stderr',
]


__author__ : str = 'Nathan Jarjarbin'
__email__ : str = 'nathan.epitech.eu'
