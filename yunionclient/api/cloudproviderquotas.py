
from yunionclient.common import base

class Cloudproviderquota(base.ResourceBase):
    pass


class CloudproviderquotaManager(base.StandaloneManager):
    resource_class = Cloudproviderquota
    keyword = 'cloudproviderquota'
    keyword_plural = 'cloudproviderquotas'
    _columns = []
    _admin_columns = []

