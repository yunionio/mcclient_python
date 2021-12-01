from yunionclient.common import base

class RouteTableAssociation(base.ResourceBase):
    pass


class RouteTableAssociationManager(base.StandaloneManager):
    resource_class = RouteTableAssociation
    keyword = 'route_table_association'
    keyword_plural = 'route_table_associations'
    _columns = ["Id", "Name", "Type", "Route_Table_Id", "Association_Type", "Associated_Resource_Id", "Ext_Associated_Resource_Id"]

