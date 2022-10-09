from yunionclient.common import base

class Dimensionjoint(base.ResourceBase):
    pass


class DimensionjointManager(base.MeterManager):
    resource_class = Dimensionjoint
    keyword = 'dimensionjoint'
    keyword_plural = 'dimensionjoints'
    _columns = ["id","name","data"]