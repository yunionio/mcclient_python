
from yunionclient.common import base

class Monitorresource(base.ResourceBase):
    pass


class MonitorresourceManager(base.StandaloneManager):
    resource_class = Monitorresource
    keyword = 'monitorresource'
    keyword_plural = 'monitorresources'
    _columns = []
    _admin_columns = []

