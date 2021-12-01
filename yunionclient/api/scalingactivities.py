from yunionclient.common import base

class Scalingactivity(base.ResourceBase):
    pass


class ScalingactivityManager(base.StandaloneManager):
    resource_class = Scalingactivity
    keyword = 'scalingactivity'
    keyword_plural = 'scalingactivities'
    _columns = ["Id", "Name", "Instance_Number", "Trigger_Desc", "Action_Desc", "Status", "Start_Time", "End_Time", "Reason"]

