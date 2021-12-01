from yunionclient.common import base

class Scheduledtask(base.ResourceBase):
    pass


class ScheduledtaskManager(base.StandaloneManager):
    resource_class = Scheduledtask
    keyword = 'scheduledtask'
    keyword_plural = 'scheduledtasks'
    _columns = ["Id", "Name", "Scheduled_Type", "Timer", "Cycle_Timer", "Resource_Type", "Operation", "Label_Type", "Labels", "Timer_Desc"]

