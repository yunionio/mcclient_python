
from yunionclient.common import base

class Clouduser(base.ResourceBase):
    pass


class ClouduserManager(base.StandaloneManager):
    resource_class = Clouduser
    keyword = 'clouduser'
    keyword_plural = 'cloudusers'
    _columns = []
    _admin_columns = []

