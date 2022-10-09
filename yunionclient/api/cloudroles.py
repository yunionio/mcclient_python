from yunionclient.common import base

class Cloudrole(base.ResourceBase):
    pass


class CloudroleManager(base.CloudidManager):
    resource_class = Cloudrole
    keyword = 'cloudrole'
    keyword_plural = 'cloudroles'
    _columns = []