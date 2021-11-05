from yunionclient.common import base

class SecgroupCache(base.ResourceBase):
    pass

class SecgroupCacheManager(base.StandaloneManager):
    resource_class = SecgroupCache
    keyword = "secgroupcache"
    keyword_plural = "secgroupcaches"
    _columns = ["ID", "Status", "Cloudaccount_id", "Cloudregion_id", "External_id", "Manager_id", "Secgroup_id", "Reference_count", "Vpc_id", "External_project_id"]

