
from yunionclient.common import base

class Instancegroup(base.ResourceBase):
    pass


class InstancegroupManager(base.StandaloneManager):
    resource_class = Instancegroup
    keyword = 'instancegroup'
    keyword_plural = 'instancegroups'
    _columns = []
    _admin_columns = []

