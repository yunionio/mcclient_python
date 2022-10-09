from yunionclient.common import base

class BillCondition(base.ResourceBase):
    pass


class BillConditionManager(base.MeterManager):
    resource_class = BillCondition
    keyword = 'bill_condition'
    keyword_plural = 'bill_conditions'
    _columns = ["item_id","item_name"]