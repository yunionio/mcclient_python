from yunionclient.common import base

class Budget(base.ResourceBase):
    pass


class BudgetManager(base.MeterManager):
    resource_class = Budget
    keyword = 'budget'
    keyword_plural = 'budgets'
    _columns = ["period_type","start_time","end_time","brand","cloudaccount_id","cloudaccount","cloudprovider_id","cloudprovider_name","region_id","region","domain_id_filter","domain_filter","project_id_filter","project_filter","resource_type","currency","amount","alerts","availability_status","budget_scope"]