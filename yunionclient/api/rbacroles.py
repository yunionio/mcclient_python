
from yunionclient.common import base

class Rbacrole(base.ResourceBase):
    pass


class RbacroleManager(base.StandaloneManager):
    resource_class = Rbacrole
    keyword = 'rbacrole'
    keyword_plural = 'rbacroles'
    _columns = []
    _admin_columns = []

