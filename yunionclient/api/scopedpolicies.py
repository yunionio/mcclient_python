from yunionclient.common import base

class Scopedpolicy(base.ResourceBase):
    pass


class ScopedpolicyManager(base.StandaloneManager):
    resource_class = Scopedpolicy
    keyword = 'scopedpolicy'
    keyword_plural = 'scopedpolicies'
    _columns = ["Id", "Name", "Category", "Policies", "Public_Scope", "Domain_Id", "Ref_Count"]

