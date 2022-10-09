from yunionclient.common import base

class ResourceFee(base.ResourceBase):
    pass


class ResourceFeeManager(base.MeterManager):
    resource_class = ResourceFee
    keyword = 'resource_fee'
    keyword_plural = 'resource_fees'
    _columns = ["baremetal_fee","server_fee","gpu_fee","disk_fee","res_fee","item_name","stat_type","stat_month","month_total"]