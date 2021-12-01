from yunionclient.common import base

class Chart(base.ResourceBase):
    pass


class ChartManager(base.StandaloneManager):
    resource_class = Chart
    keyword = 'chart'
    keyword_plural = 'charts'
    _columns = ["Repowithname", "Version", "Description"]

