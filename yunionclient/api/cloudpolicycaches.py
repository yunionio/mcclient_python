from yunionclient.common import base

class Cloudpolicycache(base.ResourceBase):
    pass


class CloudpolicycacheManager(base.CloudidManager):
    resource_class = Cloudpolicycache
    keyword = 'cloudpolicycache'
    keyword_plural = 'cloudpolicycaches'
    _columns = []