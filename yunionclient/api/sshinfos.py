from yunionclient.common import base

class Sshinfo(base.ResourceBase):
    pass


class SshinfoManager(base.StandaloneManager):
    resource_class = Sshinfo
    keyword = 'sshinfo'
    keyword_plural = 'sshinfos'
    _columns = ["Id", "Server_Id", "Server_Name", "Server_Hypervisor", "Forward_Id", "User", "Host", "Port", "Need_Clean", "Failed_Reason"]

