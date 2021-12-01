
from yunionclient.common import base

class WafInstance(base.ResourceBase):
    pass


class WafInstanceManager(base.StandaloneManager):
    resource_class = WafInstance
    keyword = 'waf_instance'
    keyword_plural = 'waf_instances'
    _columns = []
    _admin_columns = []

