from yunionclient.common import base

class Loadbalancerlistener(base.ResourceBase):
    pass


class LoadbalancerlistenerManager(base.StandaloneManager):
    resource_class = Loadbalancerlistener
    keyword = 'loadbalancerlistener'
    keyword_plural = 'loadbalancerlisteners'
    _columns = ["Id", "Name", "Loadbalancer_Id", "Status", "Listener_Type", "Listener_Port", "Backend_Port", "Egress_Mbps", "Acl_Status", "Acl_Type", "Tenant"]

