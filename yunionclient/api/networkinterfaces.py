
from yunionclient.common import base

class Networkinterface(base.ResourceBase):
    pass


class NetworkinterfaceManager(base.StandaloneManager):
    resource_class = Networkinterface
    keyword = 'networkinterface'
    keyword_plural = 'networkinterfaces'
    _columns = []
    _admin_columns = []

