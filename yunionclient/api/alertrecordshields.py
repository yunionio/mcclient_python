
from yunionclient.common import base

class Alertrecordshield(base.ResourceBase):
    pass


class AlertrecordshieldManager(base.StandaloneManager):
    resource_class = Alertrecordshield
    keyword = 'alertrecordshield'
    keyword_plural = 'alertrecordshields'
    _columns = []
    _admin_columns = []

