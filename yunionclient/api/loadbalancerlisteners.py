
from yunionclient.common import base

class Loadbalancerlistener(base.ResourceBase):
    pass


class LoadbalancerlistenerManager(base.StandaloneManager):
    resource_class = Loadbalancerlistener
    keyword = 'loadbalancerlistener'
    keyword_plural = 'loadbalancerlisteners'
    _columns = []
    _admin_columns = []

