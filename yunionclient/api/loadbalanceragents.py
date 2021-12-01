
from yunionclient.common import base

class Loadbalanceragent(base.ResourceBase):
    pass


class LoadbalanceragentManager(base.StandaloneManager):
    resource_class = Loadbalanceragent
    keyword = 'loadbalanceragent'
    keyword_plural = 'loadbalanceragents'
    _columns = []
    _admin_columns = []

