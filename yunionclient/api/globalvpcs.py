
from yunionclient.common import base

class Globalvpc(base.ResourceBase):
    pass


class GlobalvpcManager(base.StandaloneManager):
    resource_class = Globalvpc
    keyword = 'globalvpc'
    keyword_plural = 'globalvpcs'
    _columns = []
    _admin_columns = []

