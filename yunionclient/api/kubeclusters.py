
from yunionclient.common import base

class Kubecluster(base.ResourceBase):
    pass


class KubeclusterManager(base.StandaloneManager):
    resource_class = Kubecluster
    keyword = 'kubecluster'
    keyword_plural = 'kubeclusters'
    _columns = []
    _admin_columns = []

