from yunionclient.common import base

class TapService(base.ResourceBase):
    pass


class TapServiceManager(base.StandaloneManager):
    resource_class = TapService
    keyword = 'tap_service'
    keyword_plural = 'tap_services'
    _columns = ["id","name","enabled","type","target_id","target","target_ips","mac_addr","flow_count"]