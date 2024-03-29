from yunionclient.common import base

class Alertpanel(base.ResourceBase):
    pass


class AlertpanelManager(base.StandaloneManager):
    resource_class = Alertpanel
    keyword = 'alertpanel'
    keyword_plural = 'alertpanels'
    _columns = ["Id", "Name", "Setting", "Common_Alert_Metric_Details"]

