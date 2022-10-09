from yunionclient.common import base

class BillBalance(base.ResourceBase):
    pass


class BillBalanceManager(base.MeterManager):
    resource_class = BillBalance
    keyword = 'bill_balance'
    keyword_plural = 'bill_balances'
    _columns = ["provider","account","account_name","query_date","balance","currency","today_fee","month_fee"]