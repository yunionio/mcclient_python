from yunionclient.common import base

class Schedpolicy(base.ResourceBase):
    pass


class SchedpolicyManager(base.StandaloneManager):
    resource_class = Schedpolicy
    keyword = 'schedpolicy'
    keyword_plural = 'schedpolicies'
    _columns = ["ID","Name","Description","Condition","Schedtag","Resource_Type","Schedtag_Id","Strategy","Enabled"]