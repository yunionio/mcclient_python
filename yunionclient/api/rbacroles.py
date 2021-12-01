from yunionclient.common import base

class Rbacrole(base.ResourceBase):
    pass


class RbacroleManager(base.StandaloneManager):
    resource_class = Rbacrole
    keyword = 'rbacrole'
    keyword_plural = 'rbacroles'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Namespace_Id", "Namespace", "Labels", "Cluster_Id", "Cluster"]

