from yunionclient.common import base

class Secgrouprule(base.ResourceBase):
    pass


class SecgroupruleManager(base.StandaloneManager):
    resource_class = Secgrouprule
    keyword = 'secgrouprule'
    keyword_plural = 'secgrouprules'
    _columns = ["Id", "Name", "Direction", "Action", "Protocol", "Ports", "Priority", "Cidr", "Secgroup", "Peer_Secgroup_Id", "Peer_Secgroup", "Tenant", "Description", "Secgroups"]

