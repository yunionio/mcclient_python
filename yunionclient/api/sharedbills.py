from yunionclient.common import base

class SharedBill(base.ResourceBase):
    pass


class SharedBillManager(base.MeterManager):
    resource_class = SharedBill
    keyword = 'shared_bill'
    keyword_plural = 'shared_bills'
    _columns = ["account","platform","region","manager_project","res_id","res_type","res_name","charge_type","res_fee"]