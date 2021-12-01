from yunionclient.common import base

class Alert(base.ResourceBase):
    pass


class AlertManager(base.StandaloneManager):
    resource_class = Alert
    keyword = 'alert'
    keyword_plural = 'alerts'
    _columns = ["Id", "Name", "Frequency", "Enabled", "Settings", "State"]

