from yunionclient.common import base

class Proxysetting(base.ResourceBase):
    pass


class ProxysettingManager(base.StandaloneManager):
    resource_class = Proxysetting
    keyword = 'proxysetting'
    keyword_plural = 'proxysettings'
    _columns = ["Id", "Name", "Http_Proxy", "Https_Proxy", "No_Proxy", "Is_Public", "Public_Scope"]

