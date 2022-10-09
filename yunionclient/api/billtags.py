from yunionclient.common import base

class BillTag(base.ResourceBase):
    pass


class BillTagManager(base.MeterManager):
    resource_class = BillTag
    keyword = 'bill_tag'
    keyword_plural = 'bill_tags'
    _columns = ["id","key","value","res_type","month_amount","year_amount"]