
from yunionclient.common import base

class RouteTable(base.ResourceBase):
    pass


class RouteTableManager(base.StandaloneManager):
    resource_class = RouteTable
    keyword = 'route_table'
    keyword_plural = 'route_tables'
    _columns = []
    _admin_columns = []

