from yunionclient.common import base

class InfrasQuota(base.ResourceBase):
    pass


class InfrasQuotaManager(base.StandaloneManager):
    resource_class = InfrasQuota
    keyword = 'infras_quota'
    keyword_plural = 'infras_quotas'
    _columns = ["Id", "Name", "Description"]

