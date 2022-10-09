from yunionclient.common import base

class Samluser(base.ResourceBase):
    pass


class SamluserManager(base.CloudidManager):
    resource_class = Samluser
    keyword = 'samluser'
    keyword_plural = 'samlusers'
    _columns = []