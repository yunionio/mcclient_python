from yunionclient.common import base

class Deployment(base.ResourceBase):
    pass


class DeploymentManager(base.StandaloneManager):
    resource_class = Deployment
    keyword = 'deployment'
    keyword_plural = 'deployments'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Namespace_Id", "Namespace", "Labels", "Cluster_Id", "Cluster"]

