from yunionclient.common import base

class EIP(base.ResourceBase):
    pass

class EIPManager(base.StandaloneManager):
    resource_class = EIP
    keyword = 'eip'
    keyword_plural = 'eips'
    _columns = ["ID", "Name", "Status", "Network_id", "Cloudaccount_id", "External_id", "Mode", "Ip_addr", "Associate_type", "Associate_id", " Bgp_type", "Charge_type", "Bandwidth"]
    _admin_columns = []
