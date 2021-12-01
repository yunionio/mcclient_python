
from yunionclient.common import base

class Scope-resource(base.ResourceBase):
    pass


class Scope-resourceManager(base.StandaloneManager):
    resource_class = Scope-resource
    keyword = 'scope-resource'
    keyword_plural = 'scope-resource'
    _columns = []
    _admin_columns = []

