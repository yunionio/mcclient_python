from yunionclient.common import base

class BillResource(base.ResourceBase):
    pass


class BillResourceManager(base.MeterManager):
    resource_class = BillResource
    keyword = 'bill_resource'
    keyword_plural = 'bill_resources'
    _columns = ["account","platform","region","manager_project","res_id","res_type","res_name","charge_type","res_fee"]