
from yunionclient.common import base

class Policy(base.ResourceBase):
    pass


class PolicyManager(base.StandaloneManager):
    resource_class = Policy
    keyword = 'policy'
    keyword_plural = 'policies'
    _columns = []
    _admin_columns = []

