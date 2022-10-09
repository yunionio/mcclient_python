from yunionclient.common import base

class TapFlow(base.ResourceBase):
    pass


class TapFlowManager(base.StandaloneManager):
    resource_class = TapFlow
    keyword = 'tap_flow'
    keyword_plural = 'tap_flows'
    _columns = ["id","name","enabled","type","tap","tap_id","source_id","source","source_ips","net_id","net","vlan_id","mac_addr","direction"]