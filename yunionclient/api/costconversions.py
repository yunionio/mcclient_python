from yunionclient.common import base

class CostConversion(base.ResourceBase):
    pass


class CostConversionManager(base.MeterManager):
    resource_class = CostConversion
    keyword = 'cost_conversion'
    keyword_plural = 'cost_conversions'
    _columns = ["is_public_cloud","brand","cloudaccount_id","cloudprovider_id","domain_id_filter","enable_date","ratio"]