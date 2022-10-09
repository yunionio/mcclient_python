from yunionclient.common import base

class Cloudgroup(base.ResourceBase):
    pass


class CloudgroupManager(base.CloudidManager):
    resource_class = Cloudgroup
    keyword = 'cloudgroup'
    keyword_plural = 'cloudgroups'
    _columns = []