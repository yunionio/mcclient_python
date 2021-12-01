from yunionclient.common import base

class DomainQuota(base.ResourceBase):
    pass


class DomainQuotaManager(base.StandaloneManager):
    resource_class = DomainQuota
    keyword = 'domain_quota'
    keyword_plural = 'domain_quotas'
    _columns = ["Id", "Name", "Description"]

