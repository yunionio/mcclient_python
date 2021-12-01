from yunionclient.common import base

class Scalingpolicy(base.ResourceBase):
    pass


class ScalingpolicyManager(base.StandaloneManager):
    resource_class = Scalingpolicy
    keyword = 'scalingpolicy'
    keyword_plural = 'scalingpolicies'
    _columns = ["Id", "Name", "Timer", "Cycle_Timer", "Alarm", "Action", "Number", "Unit", "Cooling_Time"]

