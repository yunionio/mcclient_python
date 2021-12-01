
from yunionclient.common import base

class ZoneQuota(base.ResourceBase):
    pass


class ZoneQuotaManager(base.StandaloneManager):
    resource_class = ZoneQuota
    keyword = 'zone_quota'
    keyword_plural = 'zone_quotas'
    _columns = []
    _admin_columns = []

