from yunionclient.common import base

class Alertdashboard(base.ResourceBase):
    pass


class AlertdashboardManager(base.StandaloneManager):
    resource_class = Alertdashboard
    keyword = 'alertdashboard'
    keyword_plural = 'alertdashboards'
    _columns = ["Id", "Name", "Refresh", "Alert_Panel_Details"]

