from yunionclient.common import base

class InterVpcNetwork(base.ResourceBase):
    pass


class InterVpcNetworkManager(base.StandaloneManager):
    resource_class = InterVpcNetwork
    keyword = 'inter_vpc_network'
    keyword_plural = 'inter_vpc_networks'
    _columns = ["Id", "Name", "Enabled", "Status", "Manager_Id", "Public_Scope", "Domain_Id", "Domain"]

