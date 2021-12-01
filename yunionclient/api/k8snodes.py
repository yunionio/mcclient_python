
from yunionclient.common import base

class K8sNode(base.ResourceBase):
    pass


class K8sNodeManager(base.StandaloneManager):
    resource_class = K8sNode
    keyword = 'k8s_node'
    keyword_plural = 'k8s_nodes'
    _columns = []
    _admin_columns = []

