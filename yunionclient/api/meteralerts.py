
from yunionclient.common import base

class Meteralert(base.ResourceBase):
    pass


class MeteralertManager(base.StandaloneManager):
    resource_class = Meteralert
    keyword = 'meteralert'
    keyword_plural = 'meteralerts'
    _columns = []
    _admin_columns = []

