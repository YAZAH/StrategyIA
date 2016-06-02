# Under MIT License, see LICENSE.txt
from RULEngine.Util.Pose import Pose, Position
from UltimateStrat.STP.Tactic.TacticBase import TacticBase
from Util.geometry import *

__author__ = 'RoboCupULaval'


class tTestPathfinder(TacticBase):
    def __init__(self):
        TacticBase.__init__(self, self.__class__.__name__)

    def apply(self, info_manager, id_player):
        bot_pst = info_manager.get_player_position(id_player)
        ball_pst = info_manager.get_ball_position()
        action = info_manager.get_player_next_action(id_player)
        if id_player == 1:
            pst = Position(1500, 1500)
        elif id_player == 2:
            pst = Position(1000, 1000)
        elif id_player == 3:
            pst = Position(500, 500)
        elif id_player == 4:
            pst = Position(0, 0)
        elif id_player == 5:
            pst = Position(-500, -500)

        if isinstance(action, list):
            return {'skill': 'sWait', 'target': bot_pst, 'goal': bot_pst}
        else:
            return {'skill': 'sPathfinder', 'target': pst, 'goal': bot_pst}


"""  Pour des tests sup'
        if id_player == 1:
            pst = Position(1500, 1500)
        elif id_player == 2:
            pst = Position(1500, 0)
        elif id_player == 3:
            pst = Position(-1500, 0)
        elif id_player == 4:
            pst = Position(-1500, 1500)
        elif id_player == 5:
            pst = Position(0, 750)"""
