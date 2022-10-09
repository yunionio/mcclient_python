from yunionclient.common import base

class CloudSkuRate(base.ResourceBase):
    pass


class CloudSkuRateManager(base.MeterManager):
    resource_class = CloudSkuRate
    keyword = 'cloud_sku_rate'
    keyword_plural = 'cloud_sku_rates'
    _columns = ["id","data_id","data_key","hour_price","month_price","year_price"]