
from yunionclient.common import base

class Namespace(base.ResourceBase):
    pass


class NamespaceManager(base.StandaloneManager):
    resource_class = Namespace
    keyword = 'namespace'
    keyword_plural = 'namespaces'
    _columns = []
    _admin_columns = []

