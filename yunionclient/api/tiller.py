
from yunionclient.common import base

class Tiller(base.ResourceBase):
    pass


class TillerManager(base.StandaloneManager):
    resource_class = Tiller
    keyword = 'tiller'
    keyword_plural = 'tiller'
    _columns = []
    _admin_columns = []

