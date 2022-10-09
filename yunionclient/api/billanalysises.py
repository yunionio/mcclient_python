from yunionclient.common import base

class BillAnalysis(base.ResourceBase):
    pass


class BillAnalysisManager(base.MeterManager):
    resource_class = BillAnalysis
    keyword = 'bill_analysis'
    keyword_plural = 'bill_analysises'
    _columns = ["stat_date","stat_value","res_name","res_type","project_name","res_fee"]