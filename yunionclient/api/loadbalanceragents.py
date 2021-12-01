from yunionclient.common import base

class Loadbalanceragent(base.ResourceBase):
    pass


class LoadbalanceragentManager(base.StandaloneManager):
    resource_class = Loadbalanceragent
    keyword = 'loadbalanceragent'
    keyword_plural = 'loadbalanceragents'
    _columns = ["Id", "Name", "Hb_Last_Seen", "Hb_Timeout", "Loadbalancers", "Loadbalancer_Listeners", "Loadbalancer_Listener_Rules", "Loadbalancer_Backend_Groups", "Loadbalancer_Backends", "Loadbalancer_Acls", "Loadbalancer_Certificates"]

