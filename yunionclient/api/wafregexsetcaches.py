from yunionclient.common import base

class WafRegexsetCache(base.ResourceBase):
    pass


class WafRegexsetCacheManager(base.StandaloneManager):
    resource_class = WafRegexsetCache
    keyword = 'waf_regexset_cache'
    keyword_plural = 'waf_regexset_caches'
    _columns = ["Id", "Name", "Status", "Cloudregion", "Provider", "Account", "Type", "Domain_Id", "Domain", "Metadata"]

