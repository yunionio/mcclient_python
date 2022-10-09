from yunionclient.common import base

class BillingExchangeRate(base.ResourceBase):
    pass


class BillingExchangeRateManager(base.MeterManager):
    resource_class = BillingExchangeRate
    keyword = 'billing_exchange_rate'
    keyword_plural = 'billing_exchange_rates'
    _columns = ["src","dest","rate","date"]