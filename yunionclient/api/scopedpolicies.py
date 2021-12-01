
from yunionclient.common import base

class Scopedpolicy(base.ResourceBase):
    pass


class ScopedpolicyManager(base.StandaloneManager):
    resource_class = Scopedpolicy
    keyword = 'scopedpolicy'
    keyword_plural = 'scopedpolicies'
    _columns = []
    _admin_columns = []

