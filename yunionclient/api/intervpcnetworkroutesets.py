from yunionclient.common import base

class InterVpcNetworkRouteSet(base.ResourceBase):
    pass


class InterVpcNetworkRouteSetManager(base.StandaloneManager):
    resource_class = InterVpcNetworkRouteSet
    keyword = 'inter_vpc_network_route_set'
    keyword_plural = 'inter_vpc_network_route_sets'
    _columns = ["Id", "Inter_Vpc_Network_Id", "Name", "Enabled", "Status", "Cidr", "Vpc_Id", "Ext_Instance_Id", "Ext_Instance_Type", "Ext_Instance_Region_Id"]

