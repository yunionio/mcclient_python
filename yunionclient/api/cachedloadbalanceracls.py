from yunionclient.common import base

class Cachedloadbalanceracl(base.ResourceBase):
    pass


class CachedloadbalanceraclManager(base.StandaloneManager):
    resource_class = Cachedloadbalanceracl
    keyword = 'cachedloadbalanceracl'
    keyword_plural = 'cachedloadbalanceracls'
    _columns = ["Id", "Acl_Id", "Name", "Acl_Entries", "Tenant"]

