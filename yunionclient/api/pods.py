from yunionclient.common import base

class Pod(base.ResourceBase):
    pass


class PodManager(base.StandaloneManager):
    resource_class = Pod
    keyword = 'pod'
    keyword_plural = 'pods'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Namespace_Id", "Namespace", "Labels", "Ip", "Restarts", "Cluster_Id", "Cluster", "Node"]

