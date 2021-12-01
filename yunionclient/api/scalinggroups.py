from yunionclient.common import base

class Scalinggroup(base.ResourceBase):
    pass


class ScalinggroupManager(base.StandaloneManager):
    resource_class = Scalinggroup
    keyword = 'scalinggroup'
    keyword_plural = 'scalinggroups'
    _columns = ["Id", "Name", "Hypervisor", "Cloudregion_Id", "Network_Id", "Min_Instance_Number", "Max_Instance_Number", "Desire_Instance_Number", "Guest_Template_Id", "Loadbalancer_Id", "Group_Id", "Enabled", "Expansion_Principle", "Shrink_Principle"]

