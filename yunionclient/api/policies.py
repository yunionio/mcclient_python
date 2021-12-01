from yunionclient.common import base

class Policy(base.ResourceBase):
    pass


class PolicyManager(base.StandaloneManager):
    resource_class = Policy
    keyword = 'policy'
    keyword_plural = 'policies'
    _columns = ["Id", "Name", "Policy", "Scope", "Enabled", "Domain_Id", "Domain", "Project_Domain", "Public_Scope", "Is_Public", "Description", "Is_System"]

