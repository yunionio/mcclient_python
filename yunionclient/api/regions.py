
from yunionclient.common import base

class Region(base.ResourceBase):
    pass


class RegionManager(base.StandaloneManager):
    resource_class = Region
    keyword = 'region'
    keyword_plural = 'regions'
    _columns = []
    _admin_columns = []

