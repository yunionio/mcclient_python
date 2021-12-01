from yunionclient.common import base

class Federatednamespace(base.ResourceBase):
    pass


class FederatednamespaceManager(base.StandaloneManager):
    resource_class = Federatednamespace
    keyword = 'federatednamespace'
    keyword_plural = 'federatednamespaces'
    _columns = ["Id", "Name", "Description"]

