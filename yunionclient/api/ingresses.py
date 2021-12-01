from yunionclient.common import base

class Ingress(base.ResourceBase):
    pass


class IngressManager(base.StandaloneManager):
    resource_class = Ingress
    keyword = 'ingress'
    keyword_plural = 'ingresses'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Namespace_Id", "Namespace", "Labels", "Cluster_Id", "Cluster"]

