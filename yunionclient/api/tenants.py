from yunionclient.common import base

from .users import User


class Tenant(base.ResourceBase):
    pass


class TenantManager(base.IdentityManager):
    resource_class = Tenant
    is_admin_api = True
    keyword = 'tenant'
    keyword_plural = 'tenants'
    _columns = ['ID', 'Name', 'Enabled']

    def list_users(self, tid):
        url = r'/tenants/%s/users' % tid
        return self._list(url, 'users', obj_class=User)
