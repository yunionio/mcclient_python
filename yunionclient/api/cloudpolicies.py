from yunionclient.common import base

class Cloudpolicy(base.ResourceBase):
    pass


class CloudpolicyManager(base.StandaloneManager):
    resource_class = Cloudpolicy
    keyword = 'cloudpolicy'
    keyword_plural = 'cloudpolicies'
    _columns = ["Id", "Name", "Description", "Domain_Id", "Domain", "Public_Scope", "Policy_Type", "Status", "Locked"]

