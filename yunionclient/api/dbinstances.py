from yunionclient.common import base

class Dbinstance(base.ResourceBase):
    pass


class DbinstanceManager(base.StandaloneManager):
    resource_class = Dbinstance
    keyword = 'dbinstance'
    keyword_plural = 'dbinstances'
    _columns = ["ID", "Name", "Billing_type", "Cloudregion_Id", "Status", "Vcpu_Count", "Vmem_Size_Mb"]
    _admin_columns = []
