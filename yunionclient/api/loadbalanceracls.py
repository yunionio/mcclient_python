
from yunionclient.common import base

class Loadbalanceracl(base.ResourceBase):
    pass


class LoadbalanceraclManager(base.StandaloneManager):
    resource_class = Loadbalanceracl
    keyword = 'loadbalanceracl'
    keyword_plural = 'loadbalanceracls'
    _columns = []
    _admin_columns = []

