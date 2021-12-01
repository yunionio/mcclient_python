from yunionclient.common import base

class Kubemachine(base.ResourceBase):
    pass


class KubemachineManager(base.StandaloneManager):
    resource_class = Kubemachine
    keyword = 'kubemachine'
    keyword_plural = 'kubemachines'
    _columns = ["Name", "Id", "Status", "Role", "First_Node", "Cluster", "Provider", "Resource_Type", "Resource_Id", "Address", "Hypervisor", "Zone_Id", "Network_Id"]

