# Under MIT License, see LICENSE.txt
from UltimateStrat.STP.Skill.SkillBase import SkillBase
from RULEngine.Util.Pose import Pose, Position

__author__ = 'RoboCupULaval'


class sPathfinder(SkillBase):
    """
    sPathfinder génère un chemin prédéfini pour les tests
    """
    def __init__(self):
        SkillBase.__init__(self, self.__class__.__name__)

    def act(self, pose_player, pose_target, pose_goal):
        """ Pour des tests sup'
        return [Pose(Position(pose_target.x, pose_target.y + 500), 90),
                Pose(Position(pose_target.x + 500, pose_target.y), 0),
                Pose(Position(pose_target.x, pose_target.y - 500), 270),
                Pose(Position(pose_target.x - 500, pose_target.y), 180)]"""

        pose_1=Position(pose_target.x, pose_target.y+1000)
        pose_2=Position(pose_target.x, pose_target.y - 1000)
        angle=90
        return [Pose(pose_1, angle),
                Pose(pose_2, angle)]
