from yunionclient.common import base

class Clouduser(base.ResourceBase):
    pass


class ClouduserManager(base.CloudidManager):
    resource_class = Clouduser
    keyword = 'clouduser'
    keyword_plural = 'cloudusers'
    _columns = []