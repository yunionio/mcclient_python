from yunionclient.common import base

class DnsZone(base.ResourceBase):
    pass


class DnsZoneManager(base.StandaloneManager):
    resource_class = DnsZone
    keyword = "dns_zone" 
    keyword_plural = "dns_zones"
    _columns = []
    _admin_columns = []
