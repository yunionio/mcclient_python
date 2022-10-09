from yunionclient.common import base

class AccountBalance(base.ResourceBase):
    pass


class AccountBalanceManager(base.MeterManager):
    resource_class = AccountBalance
    keyword = 'account_balance'
    keyword_plural = 'account_balances'
    _columns = ["account_type","available_amount","current_outcome","current_income"]