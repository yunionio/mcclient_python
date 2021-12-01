
from yunionclient.common import base

class Networkaddress(base.ResourceBase):
    pass


class NetworkaddressManager(base.StandaloneManager):
    resource_class = Networkaddress
    keyword = 'networkaddress'
    keyword_plural = 'networkaddresses'
    _columns = []
    _admin_columns = []

