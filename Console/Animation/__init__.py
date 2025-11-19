#############################
###                       ###
###      Console v2.0     ###
###  ----__init__.py----  ###
###                       ###
###=======================###
### by JARJARBIN's STUDIO ###
#############################


from Console.Animation.animation import Animation
from Console.Animation.basepack import BasePack
from Console.Animation.progressbar import ProgressBar
from Console.Animation.style import Style
from Console.Animation.spinner import Spinner


__all__ : list[str] = [
    'Animation',
    'BasePack',
    'ProgressBar',
    'Style',
    'Spinner'
]


__author__ : str = 'Nathan Jarjarbin'
__email__ : str = 'nathan.epitech.eu'


BasePack.update()
