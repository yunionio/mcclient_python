from yunionclient.common import base

class Loadbalancercluster(base.ResourceBase):
    pass


class LoadbalancerclusterManager(base.StandaloneManager):
    resource_class = Loadbalancercluster
    keyword = 'loadbalancercluster'
    keyword_plural = 'loadbalancerclusters'
    _columns = ["Id", "Name", "Zone_Id", "Wire_Id"]

