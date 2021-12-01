
from yunionclient.common import base

class Proxysetting(base.ResourceBase):
    pass


class ProxysettingManager(base.StandaloneManager):
    resource_class = Proxysetting
    keyword = 'proxysetting'
    keyword_plural = 'proxysettings'
    _columns = []
    _admin_columns = []

