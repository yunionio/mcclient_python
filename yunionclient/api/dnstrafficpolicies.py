
from yunionclient.common import base

class DnsTrafficpolicy(base.ResourceBase):
    pass


class DnsTrafficpolicyManager(base.StandaloneManager):
    resource_class = DnsTrafficpolicy
    keyword = 'dns_trafficpolicy'
    keyword_plural = 'dns_trafficpolicies'
    _columns = []
    _admin_columns = []

