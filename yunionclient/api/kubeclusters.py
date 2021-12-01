from yunionclient.common import base

class Kubecluster(base.ResourceBase):
    pass


class KubeclusterManager(base.StandaloneManager):
    resource_class = Kubecluster
    keyword = 'kubecluster'
    keyword_plural = 'kubeclusters'
    _columns = ["Name", "Id", "Status", "Cluster_Type", "Cloudregion_Id", "Vpc_Id", "Resource_Type", "Cloud_Type", "Version", "Mode", "Provider", "Machines", "Sync_Status", "Sync_Message"]

