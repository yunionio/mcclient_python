from yunionclient.common import base

class Metricmeasurement(base.ResourceBase):
    pass


class MetricmeasurementManager(base.StandaloneManager):
    resource_class = Metricmeasurement
    keyword = 'metricmeasurement'
    keyword_plural = 'metricmeasurements'
    _columns = ["Id", "Name", "Display_Name", "Res_Type", "Metric_Fields"]

