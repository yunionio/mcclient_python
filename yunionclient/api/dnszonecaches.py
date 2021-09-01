from yunionclient.common import base

class DnsZoneCache(base.ResourceBase):
    pass

class DnsZoneCacheManager(base.StandaloneManager):
    resource_class = DnsZoneCache
    keyword = 'dns_zonecache'
    keyword_plural = 'dns_zonecaches'
    _columns = ["ID", "Name", "Status", "Dns_zone_id", "Cloudaccount_id", "External_id"]
    _admin_columns = []
