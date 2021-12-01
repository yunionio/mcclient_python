
from yunionclient.common import base

class Metricmeasurement(base.ResourceBase):
    pass


class MetricmeasurementManager(base.StandaloneManager):
    resource_class = Metricmeasurement
    keyword = 'metricmeasurement'
    keyword_plural = 'metricmeasurements'
    _columns = []
    _admin_columns = []

