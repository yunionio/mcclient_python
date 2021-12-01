from yunionclient.common import base

class Statefulset(base.ResourceBase):
    pass


class StatefulsetManager(base.StandaloneManager):
    resource_class = Statefulset
    keyword = 'statefulset'
    keyword_plural = 'statefulsets'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Namespace_Id", "Namespace", "Labels", "Cluster_Id", "Cluster"]

