from yunionclient.common import base

class Daemonset(base.ResourceBase):
    pass


class DaemonsetManager(base.StandaloneManager):
    resource_class = Daemonset
    keyword = 'daemonset'
    keyword_plural = 'daemonsets'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Namespace_Id", "Namespace", "Labels", "Cluster_Id", "Cluster"]

