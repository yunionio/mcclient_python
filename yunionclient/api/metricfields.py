
from yunionclient.common import base

class Metricfield(base.ResourceBase):
    pass


class MetricfieldManager(base.StandaloneManager):
    resource_class = Metricfield
    keyword = 'metricfield'
    keyword_plural = 'metricfields'
    _columns = []
    _admin_columns = []

