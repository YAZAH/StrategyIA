#Under MIT License, see LICENSE.txt
from ai.STP.Skill.SkillBase import SkillBase
from RULEngine.Util.Pose import Pose

__author__ = 'RoboCupULaval'


class sGoToTarget(SkillBase):
    """
    sGoToTarget generate next pose which is target pose
    """
    def __init__(self):
        SkillBase.__init__(self, self.__class__.__name__)

    def act(self, pose_player, pose_target, pose_goal):
        return Pose(pose_target, pose_player.orientation)
