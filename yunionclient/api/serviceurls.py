from yunionclient.common import base

class Serviceurl(base.ResourceBase):
    pass


class ServiceurlManager(base.StandaloneManager):
    resource_class = Serviceurl
    keyword = 'serviceurl'
    keyword_plural = 'serviceurls'
    _columns = ["Id", "Service", "Server_Id", "Url", "Server_Ansible_Info", "Failed_Reason"]

