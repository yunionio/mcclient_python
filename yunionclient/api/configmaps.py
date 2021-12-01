
from yunionclient.common import base

class Configmap(base.ResourceBase):
    pass


class ConfigmapManager(base.StandaloneManager):
    resource_class = Configmap
    keyword = 'configmap'
    keyword_plural = 'configmaps'
    _columns = []
    _admin_columns = []

