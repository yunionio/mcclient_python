from yunionclient.common import base

class WafIpsetCache(base.ResourceBase):
    pass


class WafIpsetCacheManager(base.StandaloneManager):
    resource_class = WafIpsetCache
    keyword = 'waf_ipset_cache'
    keyword_plural = 'waf_ipset_caches'
    _columns = ["Id", "Name", "Status", "Cloudregion", "Provider", "Account", "Type", "Domain_Id", "Domain", "Metadata"]

