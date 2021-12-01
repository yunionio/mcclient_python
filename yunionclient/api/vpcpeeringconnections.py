
from yunionclient.common import base

class VpcPeeringConnection(base.ResourceBase):
    pass


class VpcPeeringConnectionManager(base.StandaloneManager):
    resource_class = VpcPeeringConnection
    keyword = 'vpc_peering_connection'
    keyword_plural = 'vpc_peering_connections'
    _columns = []
    _admin_columns = []

