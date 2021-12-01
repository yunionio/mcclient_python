from yunionclient.common import base

class Natdentry(base.ResourceBase):
    pass


class NatdentryManager(base.StandaloneManager):
    resource_class = Natdentry
    keyword = 'natdentry'
    keyword_plural = 'natdentries'
    _columns = ["Id", "Name", "Status", "Natgateway_Id", "Natgateway", "External_Ip", "External_Port", "Internal_Ip", "Internal_Port", "Ip_Protocol"]

