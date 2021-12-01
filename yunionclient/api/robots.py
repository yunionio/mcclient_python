from yunionclient.common import base

class Robot(base.ResourceBase):
    pass


class RobotManager(base.StandaloneManager):
    resource_class = Robot
    keyword = 'robot'
    keyword_plural = 'robots'
    _columns = ["Id", "Name", "Type", "Address", "Lang"]

