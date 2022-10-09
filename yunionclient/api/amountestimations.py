from yunionclient.common import base

class AmountEstimation(base.ResourceBase):
    pass


class AmountEstimationManager(base.MeterManager):
    resource_class = AmountEstimation
    keyword = 'amount_estimation'
    keyword_plural = 'amount_estimations'
    _columns = ["amount"]