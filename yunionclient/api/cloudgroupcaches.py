from yunionclient.common import base

class Cloudgroupcache(base.ResourceBase):
    pass


class CloudgroupcacheManager(base.CloudidManager):
    resource_class = Cloudgroupcache
    keyword = 'cloudgroupcache'
    keyword_plural = 'cloudgroupcaches'
    _columns = []