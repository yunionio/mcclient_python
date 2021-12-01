
from yunionclient.common import base

class Notifytemplate(base.ResourceBase):
    pass


class NotifytemplateManager(base.StandaloneManager):
    resource_class = Notifytemplate
    keyword = 'notifytemplate'
    keyword_plural = 'notifytemplates'
    _columns = []
    _admin_columns = []

