
from yunionclient.common import base

class Deployment(base.ResourceBase):
    pass


class DeploymentManager(base.StandaloneManager):
    resource_class = Deployment
    keyword = 'deployment'
    keyword_plural = 'deployments'
    _columns = []
    _admin_columns = []

