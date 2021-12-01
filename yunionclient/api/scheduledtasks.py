
from yunionclient.common import base

class Scheduledtask(base.ResourceBase):
    pass


class ScheduledtaskManager(base.StandaloneManager):
    resource_class = Scheduledtask
    keyword = 'scheduledtask'
    keyword_plural = 'scheduledtasks'
    _columns = []
    _admin_columns = []

