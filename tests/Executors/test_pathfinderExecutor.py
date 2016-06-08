#Under MIT License, see LICENSE.txt
# TODO Faire des tests quand le pathfinder sera implemente
from unittest import TestCase

from ai.Executor.PathfinderExecutor import *


from RULEngine.Game.Field import Field
from RULEngine.Game.Ball import Ball
from RULEngine.Game.Team import Team
from RULEngine.Game.Player import Player
from RULEngine.Util.Pose import Pose, Position

__author__ = 'RoboCupULaval'


class TestPathfinderExecutor(TestCase):
    """Tests de la classe PathfinderExecutor"""

    def setUp(self):
        self.current_skill = None
        self.current_target = Pose(Position(0, 0), 0)
        self.current_goal = Pose(Position(1, 1), 1)

        # Initialisation de l'InfoManager avec des équipes de robots et une balle
        self.team = Team([Player(bot_id) for bot_id in range(6)], True)
        for player in self.team.players:
            self.team.players[player.id].position = Position(100 * player.id, 100 * player.id)

        self.op_team = Team([Player(bot_id) for bot_id in range(6)], False)
        for player in self.op_team.players:
            self.op_team.players[player.id].position = Position(-100 * player.id - 100, -100 * player.id - 100)

        self.field = Field(Ball())
        self.field.ball.set_position(Position(1000, 0), 1)
        self.info = InfoManager(self.field, self.team, self.op_team)

    def test_execSkillnNull(self):
        """Test la fonction exec si current_Skill == None"""
        self.assertRaises(Exception,self.current_skill,None)






