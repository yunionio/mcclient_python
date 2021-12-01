
from yunionclient.common import base

class Loadbalancerbackend(base.ResourceBase):
    pass


class LoadbalancerbackendManager(base.StandaloneManager):
    resource_class = Loadbalancerbackend
    keyword = 'loadbalancerbackend'
    keyword_plural = 'loadbalancerbackends'
    _columns = []
    _admin_columns = []

