from yunionclient.common import base

class Billsdimension(base.ResourceBase):
    pass


class BillsdimensionManager(base.MeterManager):
    resource_class = Billsdimension
    keyword = 'billsdimension'
    keyword_plural = 'billsdimensions'
    _columns = ["id","name","dimension_type","dimension_items"]