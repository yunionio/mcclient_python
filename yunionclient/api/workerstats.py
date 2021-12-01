
from yunionclient.common import base

class Workers(base.ResourceBase):
    pass


class WorkersManager(base.StandaloneManager):
    resource_class = Workers
    keyword = 'workers'
    keyword_plural = 'worker_stats'
    _columns = []
    _admin_columns = []

