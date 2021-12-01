from yunionclient.common import base

class WafInstance(base.ResourceBase):
    pass


class WafInstanceManager(base.StandaloneManager):
    resource_class = WafInstance
    keyword = 'waf_instance'
    keyword_plural = 'waf_instances'
    _columns = ["Id", "Name", "Enabled", "Status", "Cloudregion_Id", "Region", "Rules", "Public_Scope", "Domain_Id", "Domain", "Metadata"]

