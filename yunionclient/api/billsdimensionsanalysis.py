from yunionclient.common import base

class Billsdimensionsanalysis(base.ResourceBase):
    pass


class BillsdimensionsanalysisManager(base.MeterManager):
    resource_class = Billsdimensionsanalysis
    keyword = 'billsdimensionsanalysis'
    keyword_plural = 'billsdimensionsanalysis'
    _columns = ["id","name","usage_type","resource_type","brand","description"]