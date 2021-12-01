from yunionclient.common import base

class Rolepolicy(base.ResourceBase):
    pass


class RolepolicyManager(base.StandaloneManager):
    resource_class = Rolepolicy
    keyword = 'rolepolicy'
    keyword_plural = 'rolepolicies'
    _columns = ["Id", "Name", "Role", "Role_Id", "Project", "Project_Id", "Policy", "Policy_Id", "Ips", "Scope"]

