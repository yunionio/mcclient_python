from yunionclient.common import base

class BillDetail(base.ResourceBase):
    pass


class BillDetailManager(base.MeterManager):
    resource_class = BillDetail
    keyword = 'bill_detail'
    keyword_plural = 'bill_details'
    _columns = ["bill_id","account","platform","region","manager_project","res_id","res_type","res_name","start_time","end_time","charge_type","item_rate","item_fee"]