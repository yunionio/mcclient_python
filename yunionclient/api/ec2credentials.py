from yunionclient.common import base


class EC2Credential(base.ResourceBase):

    def _get_user(self):
        if getattr(self, '_user', None) is None:
            self._user = self._client_api.users.get(self.user_id)
        return self._user

    def _get_tenant(self):
        if getattr(self, '_tenant', None) is None:
            self._tenant = self._client_api.tenants.get(self.tenant_id)
        return self._tenant

    @property
    def user_name(self):
        return self._get_user().name

    @property
    def tenant_name(self):
        return self._get_tenant().name


class EC2CredentialManager(base.IdentityManager):
    resource_class = EC2Credential
    is_admin_api = True
    keyword = 'credential'
    keyword_plural = 'credentials'
    _columns = ['Access', 'Secret', 'User_ID', 'User_Name', 'Tenant_ID',
                                                            'Tenant_Name']

    def create_ec2cred(self, uid, tid):
        params = {'tenant_id': tid}
        return self._create('/users/%s/credentials/OS-EC2' % uid,
                            params, self.keyword)

    def list_ec2cred(self, uid):
        return self._list("/users/%s/credentials/OS-EC2" % uid,
                            self.keyword_plural)

    def get_ec2cred(self, uid, access):
        return self._get("/users/%s/credentials/OS-EC2/%s" %
                         (uid, access), self.keyword)

    def delete_ec2cred(self, uid, access):
        return self._delete("/users/%s/credentials/OS-EC2/%s" %
                                (uid, access), self.keyword)
