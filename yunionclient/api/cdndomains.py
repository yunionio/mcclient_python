from yunionclient.common import base

class CdnDomain(base.ResourceBase):
    pass

class CdnDomainManager(base.StandaloneManager):
    resource_class = CdnDomain
    keyword = 'cdn_domain'
    keyword_plural = 'cdn_domains'
    _columns = ["ID", "Name", "Status", "Cloudaccount_id", "External_id", "Cname", "Origins", "ServiceType", "Area"]
    _admin_columns = []
