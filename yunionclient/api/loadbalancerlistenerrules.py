
from yunionclient.common import base

class Loadbalancerlistenerrule(base.ResourceBase):
    pass


class LoadbalancerlistenerruleManager(base.StandaloneManager):
    resource_class = Loadbalancerlistenerrule
    keyword = 'loadbalancerlistenerrule'
    keyword_plural = 'loadbalancerlistenerrules'
    _columns = []
    _admin_columns = []

