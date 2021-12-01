
from yunionclient.common import base

class Cloudgroupcache(base.ResourceBase):
    pass


class CloudgroupcacheManager(base.StandaloneManager):
    resource_class = Cloudgroupcache
    keyword = 'cloudgroupcache'
    keyword_plural = 'cloudgroupcaches'
    _columns = []
    _admin_columns = []

