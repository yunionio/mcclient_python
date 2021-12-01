from yunionclient.common import base

class Workers(base.ResourceBase):
    pass


class WorkersManager(base.StandaloneManager):
    resource_class = Workers
    keyword = 'workers'
    keyword_plural = 'worker_stats'
    _columns = ["Name", "Queue_Cnt", "Active_Worker_Cnt", "Backlog", "Detach_Worker_Cnt", "Max_Worker_Cnt"]

