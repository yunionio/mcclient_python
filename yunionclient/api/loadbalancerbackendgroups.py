
from yunionclient.common import base

class Loadbalancerbackendgroup(base.ResourceBase):
    pass


class LoadbalancerbackendgroupManager(base.StandaloneManager):
    resource_class = Loadbalancerbackendgroup
    keyword = 'loadbalancerbackendgroup'
    keyword_plural = 'loadbalancerbackendgroups'
    _columns = []
    _admin_columns = []

