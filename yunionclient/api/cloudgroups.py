
from yunionclient.common import base

class Cloudgroup(base.ResourceBase):
    pass


class CloudgroupManager(base.StandaloneManager):
    resource_class = Cloudgroup
    keyword = 'cloudgroup'
    keyword_plural = 'cloudgroups'
    _columns = []
    _admin_columns = []

