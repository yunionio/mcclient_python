from yunionclient.common import base

class CloudKubeNodePool(base.ResourceBase):
    pass


class CloudKubeNodePoolManager(base.StandaloneManager):
    resource_class = CloudKubeNodePool
    keyword = 'cloud_kube_node_pool'
    keyword_plural = 'cloud_kube_node_pools'
    _columns = ["Id", "Name", "Description"]

