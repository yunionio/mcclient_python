from yunionclient.common import base

class BillCloudcheck(base.ResourceBase):
    pass


class BillCloudcheckManager(base.MeterManager):
    resource_class = BillCloudcheck
    keyword = 'bill_cloudcheck'
    keyword_plural = 'bill_cloudchecks'
    _columns = ["provider","account_id","sum_month","res_type","res_id","res_name","external_id","cloud_fee","kvm_fee","diff_fee","diff_percent"]