from yunionclient.common import base

class Loadbalancerlistenerrule(base.ResourceBase):
    pass


class LoadbalancerlistenerruleManager(base.StandaloneManager):
    resource_class = Loadbalancerlistenerrule
    keyword = 'loadbalancerlistenerrule'
    keyword_plural = 'loadbalancerlistenerrules'
    _columns = ["Id", "Name", "Listener_Id", "Status", "Domain", "Path", "Backend_Id", "Tenant"]

