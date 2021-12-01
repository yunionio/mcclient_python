from yunionclient.common import base

class CloudKubeCluster(base.ResourceBase):
    pass


class CloudKubeClusterManager(base.StandaloneManager):
    resource_class = CloudKubeCluster
    keyword = 'cloud_kube_cluster'
    keyword_plural = 'cloud_kube_clusters'
    _columns = ["Id", "Name", "Description"]

