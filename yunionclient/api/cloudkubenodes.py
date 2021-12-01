from yunionclient.common import base

class CloudKubeNode(base.ResourceBase):
    pass


class CloudKubeNodeManager(base.StandaloneManager):
    resource_class = CloudKubeNode
    keyword = 'cloud_kube_node'
    keyword_plural = 'cloud_kube_nodes'
    _columns = ["Id", "Name", "Description"]

