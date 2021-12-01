
from yunionclient.common import base

class RouteTableAssociation(base.ResourceBase):
    pass


class RouteTableAssociationManager(base.StandaloneManager):
    resource_class = RouteTableAssociation
    keyword = 'route_table_association'
    keyword_plural = 'route_table_associations'
    _columns = []
    _admin_columns = []

