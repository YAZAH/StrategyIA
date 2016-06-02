# Under MIT License, see LICENSE.txt
from UltimateStrat.STP.Play.PlayBase import PlayBase

__author__ = 'RoboCupULaval'

SEQUENCE_PATHFINDER = ['tPathfinder', 'tTestPathfinder', 'tTestPathfinder', 'tTestPathfinder', 'tTestPathfinder',
                       'tTestPathfinder']


class pPathfinder(PlayBase):
    def __init__(self):
        PlayBase.__init__(self, self.__class__.__name__)
        self._sequence = SEQUENCE_PATHFINDER

    def getTactics(self, index=None):
        if index is None:
            return self._sequence
        else:
            return self._sequence[index]
