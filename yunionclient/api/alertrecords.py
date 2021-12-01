
from yunionclient.common import base

class Alertrecord(base.ResourceBase):
    pass


class AlertrecordManager(base.StandaloneManager):
    resource_class = Alertrecord
    keyword = 'alertrecord'
    keyword_plural = 'alertrecords'
    _columns = []
    _admin_columns = []

