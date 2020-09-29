from yunionclient.common import base


class Domain(base.ResourceBase):
    pass


class DomainManager(base.IdentityManager):
    resource_class = Domain
    is_admin_api = True
    keyword = 'domain'
    keyword_plural = 'domains'
    _columns = ['ID', 'Name', 'Enabled', 'Domain_Id', 'Parent_Id']
