
from yunionclient.common import base

class Service-registry(base.ResourceBase):
    pass


class Service-registryManager(base.StandaloneManager):
    resource_class = Service-registry
    keyword = 'service-registry'
    keyword_plural = 'service-registries'
    _columns = []
    _admin_columns = []

