from yunionclient.common import base

class Commonalert(base.ResourceBase):
    pass


class CommonalertManager(base.StandaloneManager):
    resource_class = Commonalert
    keyword = 'commonalert'
    keyword_plural = 'commonalerts'
    _columns = ["Id", "Name", "Enabled", "Level", "Alert_Type", "Period", "Recipients", "Channel"]

