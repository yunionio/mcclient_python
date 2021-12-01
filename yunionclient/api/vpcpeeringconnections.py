from yunionclient.common import base

class VpcPeeringConnection(base.ResourceBase):
    pass


class VpcPeeringConnectionManager(base.StandaloneManager):
    resource_class = VpcPeeringConnection
    keyword = 'vpc_peering_connection'
    keyword_plural = 'vpc_peering_connections'
    _columns = ["Id", "Name", "Enabled", "Status", "Vpc_Id", "Peer_Vpc_Id", "Peer_Account_Id", "Public_Scope", "Domain_Id", "Domain"]

