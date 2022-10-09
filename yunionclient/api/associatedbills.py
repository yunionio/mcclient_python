from yunionclient.common import base

class AssociatedBill(base.ResourceBase):
    pass


class AssociatedBillManager(base.MeterManager):
    resource_class = AssociatedBill
    keyword = 'associated_bill'
    keyword_plural = 'associated_bills'
    _columns = ["account","brand","resource_id","resource_name","amount"]