
from yunionclient.common import base

class Scalingpolicy(base.ResourceBase):
    pass


class ScalingpolicyManager(base.StandaloneManager):
    resource_class = Scalingpolicy
    keyword = 'scalingpolicy'
    keyword_plural = 'scalingpolicies'
    _columns = []
    _admin_columns = []

