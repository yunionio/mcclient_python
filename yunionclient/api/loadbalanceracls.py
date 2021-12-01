from yunionclient.common import base

class Loadbalanceracl(base.ResourceBase):
    pass


class LoadbalanceraclManager(base.StandaloneManager):
    resource_class = Loadbalanceracl
    keyword = 'loadbalanceracl'
    keyword_plural = 'loadbalanceracls'
    _columns = ["Id", "Name", "Project", "Is_Public", "Acl_Entries", "Tenant"]

