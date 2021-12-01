
from yunionclient.common import base

class Sshinfo(base.ResourceBase):
    pass


class SshinfoManager(base.StandaloneManager):
    resource_class = Sshinfo
    keyword = 'sshinfo'
    keyword_plural = 'sshinfos'
    _columns = []
    _admin_columns = []

