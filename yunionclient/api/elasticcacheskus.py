
from yunionclient.common import base

class Elasticcachesku(base.ResourceBase):
    pass


class ElasticcacheskuManager(base.StandaloneManager):
    resource_class = Elasticcachesku
    keyword = 'elasticcachesku'
    keyword_plural = 'elasticcacheskus'
    _columns = []
    _admin_columns = []

