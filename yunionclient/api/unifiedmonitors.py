
from yunionclient.common import base

class Unifiedmonitor(base.ResourceBase):
    pass


class UnifiedmonitorManager(base.StandaloneManager):
    resource_class = Unifiedmonitor
    keyword = 'unifiedmonitor'
    keyword_plural = 'unifiedmonitors'
    _columns = []
    _admin_columns = []

