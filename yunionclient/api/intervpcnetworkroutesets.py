
from yunionclient.common import base

class InterVpcNetworkRouteSet(base.ResourceBase):
    pass


class InterVpcNetworkRouteSetManager(base.StandaloneManager):
    resource_class = InterVpcNetworkRouteSet
    keyword = 'inter_vpc_network_route_set'
    keyword_plural = 'inter_vpc_network_route_sets'
    _columns = []
    _admin_columns = []

