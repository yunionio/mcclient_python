
from yunionclient.common import base

class Daemonset(base.ResourceBase):
    pass


class DaemonsetManager(base.StandaloneManager):
    resource_class = Daemonset
    keyword = 'daemonset'
    keyword_plural = 'daemonsets'
    _columns = []
    _admin_columns = []

