from yunionclient.common import base

class RegionQuota(base.ResourceBase):
    pass


class RegionQuotaManager(base.StandaloneManager):
    resource_class = RegionQuota
    keyword = 'region_quota'
    keyword_plural = 'region_quotas'
    _columns = ["Id", "Name", "Description"]

