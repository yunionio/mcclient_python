from yunionclient.common import base

class Ipv6Gateway(base.ResourceBase):
    pass


class Ipv6GatewayManager(base.StandaloneManager):
    resource_class = Ipv6Gateway
    keyword = 'ipv6_gateway'
    keyword_plural = 'ipv6_gateways'
    _columns = []