from yunionclient.common import base

class Natsentry(base.ResourceBase):
    pass


class NatsentryManager(base.StandaloneManager):
    resource_class = Natsentry
    keyword = 'natsentry'
    keyword_plural = 'natsentries'
    _columns = ["Id", "Name", "Status", "Ip", "Natgateway_Id", "Natgateway", "Network", "Network_Id", "Source_Cidr"]

