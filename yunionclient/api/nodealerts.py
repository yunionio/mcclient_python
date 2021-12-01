
from yunionclient.common import base

class Nodealert(base.ResourceBase):
    pass


class NodealertManager(base.StandaloneManager):
    resource_class = Nodealert
    keyword = 'nodealert'
    keyword_plural = 'nodealerts'
    _columns = []
    _admin_columns = []

