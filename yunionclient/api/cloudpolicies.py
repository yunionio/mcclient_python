
from yunionclient.common import base

class Cloudpolicy(base.ResourceBase):
    pass


class CloudpolicyManager(base.StandaloneManager):
    resource_class = Cloudpolicy
    keyword = 'cloudpolicy'
    keyword_plural = 'cloudpolicies'
    _columns = []
    _admin_columns = []

