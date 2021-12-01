from yunionclient.common import base

class Networkaddress(base.ResourceBase):
    pass


class NetworkaddressManager(base.StandaloneManager):
    resource_class = Networkaddress
    keyword = 'networkaddress'
    keyword_plural = 'networkaddresses'
    _columns = ["Id", "Type", "Parent_Type", "Parent_Id", "Network_Id", "Ip_Addr"]

