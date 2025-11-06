from yunionclient.common import base

class RateSet(base.ResourceBase):
    pass


class RateSetManager(base.MeterManager):
    resource_class = RateSet
    keyword = 'rateset'
    keyword_plural = 'ratesets'
    _columns = ["id","name","description","created_at","updated_at"]