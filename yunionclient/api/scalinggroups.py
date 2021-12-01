
from yunionclient.common import base

class Scalinggroup(base.ResourceBase):
    pass


class ScalinggroupManager(base.StandaloneManager):
    resource_class = Scalinggroup
    keyword = 'scalinggroup'
    keyword_plural = 'scalinggroups'
    _columns = []
    _admin_columns = []

