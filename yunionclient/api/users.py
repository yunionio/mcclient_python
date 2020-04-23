from yunionclient.common import base
from yunionclient.common import exceptions
from .roles import Role


class User(base.ResourceBase):

    def _get_tenant(self):
        if getattr(self, '_tenant', None) is None:
            try:
                self._tenant = self._client_api.tenants.get(self.tenantId)
            except exceptions.NotFound:
                self._tenant = None
        return self._tenant

    @property
    def tenant_name(self):
        t = self._get_tenant()
        if t is not None:
            return t.name
        else:
            return '[Deleted tenant]'


class UserManager(base.IdentityManager):
    resource_class = User
    is_admin_api = True
    keyword = 'user'
    keyword_plural = 'users'
    _columns = ['ID', 'Name', 'Enabled', 'Email', 'Mobile']

    def update_password(self, uid, password):
        params = {self.keyword: {"id": uid, "password": password}}
        return self._update("/users/%s/password" % uid, params,
                            self.keyword)

    def roles_for_user(self, uid, tid=None):
        url = r'/users/%s/roles' % uid
        if tid:
            url = r'/tenants/%s%s' % (tid, url)
        return self._list(url, 'roles', obj_class=Role)

    def add_role(self, uid, rid, tid=None):
        url = r'/users/%s/roles/%s' % (uid, rid)
        if tid:
            url = r'/tenants/%s%s' % (tid, url)
            keyword = 'role'
        else:
            keyword = 'roles'
        return self._update(url, None, keyword, obj_class=Role)

    def remove_role(self, uid, rid, tid=None):
        url = r'/users/%s/roles/%s' % (uid, rid)
        if tid:
            url = r'/tenants/%s%s' % (tid, url)
        return self._delete(url, 'roles', obj_class=Role)
