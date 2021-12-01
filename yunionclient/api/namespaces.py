from yunionclient.common import base

class Namespace(base.ResourceBase):
    pass


class NamespaceManager(base.StandaloneManager):
    resource_class = Namespace
    keyword = 'namespace'
    keyword_plural = 'namespaces'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Cluster_Id", "Cluster"]

