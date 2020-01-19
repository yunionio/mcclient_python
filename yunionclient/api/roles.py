from yunionclient.common import base


class Role(base.ResourceBase):
    pass


class RoleManager(base.IdentityManager):
    is_admin_api = True
    keyword = 'role'
    keyword_plural = 'roles'
    _columns = ['ID', 'Name', 'Description', 'Is_Public']
