
from yunionclient.common import base

class RouteTableRouteSet(base.ResourceBase):
    pass


class RouteTableRouteSetManager(base.StandaloneManager):
    resource_class = RouteTableRouteSet
    keyword = 'route_table_route_set'
    keyword_plural = 'route_table_route_sets'
    _columns = []
    _admin_columns = []

