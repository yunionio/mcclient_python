
from yunionclient.common import base

class Notifyconfig(base.ResourceBase):
    pass


class NotifyconfigManager(base.StandaloneManager):
    resource_class = Notifyconfig
    keyword = 'notifyconfig'
    keyword_plural = 'notifyconfigs'
    _columns = []
    _admin_columns = []

