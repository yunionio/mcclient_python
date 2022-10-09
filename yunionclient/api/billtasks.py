from yunionclient.common import base

class BillTask(base.ResourceBase):
    pass


class BillTaskManager(base.MeterManager):
    resource_class = BillTask
    keyword = 'bill_task'
    keyword_plural = 'bill_tasks'
    _columns = ["status"]