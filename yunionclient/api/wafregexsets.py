from yunionclient.common import base

class WafRegexset(base.ResourceBase):
    pass


class WafRegexsetManager(base.StandaloneManager):
    resource_class = WafRegexset
    keyword = 'waf_regexset'
    keyword_plural = 'waf_regexsets'
    _columns = ["Id", "Name", "Status", "Addresses", "Domain_Id", "Domain", "Metadata"]

