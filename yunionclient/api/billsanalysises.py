from yunionclient.common import base

class Billsanalysis(base.ResourceBase):
    pass


class BillsanalysisManager(base.MeterManager):
    resource_class = Billsanalysis
    keyword = 'billsanalysis'
    keyword_plural = 'billsanalysises'
    _columns = ["project","project_id","domain","domain_id","amount","year_amount"]