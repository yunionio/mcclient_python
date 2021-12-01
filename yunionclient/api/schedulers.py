from yunionclient.common import base

class Scheduler(base.ResourceBase):
    pass


class SchedulerManager(base.StandaloneManager):
    resource_class = Scheduler
    keyword = 'scheduler'
    keyword_plural = 'schedulers'
    _columns = ["Id", "Name", "Description"]

