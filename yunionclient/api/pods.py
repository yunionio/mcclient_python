
from yunionclient.common import base

class Pod(base.ResourceBase):
    pass


class PodManager(base.StandaloneManager):
    resource_class = Pod
    keyword = 'pod'
    keyword_plural = 'pods'
    _columns = []
    _admin_columns = []

