from yunionclient.common import base


class QuotaManager(base.Manager):

    def get(self, tenant, user):
        url = r'/quotas'
        if tenant is not None and len(tenant) > 0:
            url += r'/%s' % tenant
            if user is not None and len(user) > 0 and user != tenant:
                url += '/%s' % user
        resp, body = self.json_request('GET', url)
        return body['quotas']

    def set(self, tenant, **kwargs):
        url = r'/quotas'
        if tenant is not None and len(tenant) > 0:
            url += r'/%s' % tenant
        body = {'quotas': kwargs}
        resp, body = self.json_request('POST', url, body=body)
        return body['quotas']

    def check(self, tenant, **kwargs):
        url = r'/quotas/%s/%s' % (tenant, 'check_quota')
        body = {'quotas': kwargs}
        resp, body = self.json_request('POST', url, body=body)
        return body['quotas']
