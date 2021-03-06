# Under MIT License, see LICENSE.txt
from unittest import TestCase

from RULEngine.Game.Field import Field
from RULEngine.Game.Ball import Ball
from RULEngine.Game.Team import Team
from RULEngine.Game.Player import Player
from RULEngine.Util.Pose import Pose, Position

from ai.STP.Tactic.tGoalKeeper import tGoalKeeper
from ai.InfoManager import InfoManager

__author__ = 'RoboCupULaval'


class TestTacticGoalKeeper(TestCase):
    """ Tests de la classe tGoalKeeper """
    def setUp(self):
        self.tactic = tGoalKeeper()

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

    def test_construction(self):
        self.assertNotEqual(self.tactic, None)
        self.assertIsInstance(self.tactic, tGoalKeeper)

    def test_name(self):
        self.assertEqual(self.tactic.name, tGoalKeeper.__name__)

    def test_return(self):
        result = self.tactic.apply(self.info, 0)
        ball_pst = self.info.get_ball_position()

        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {'skill': 'sGoBehindTargetGoal_GK', 'target': ball_pst, 'goal': Position(-4500, 0)})
