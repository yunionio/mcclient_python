from yunionclient.common import base

class Cloudpolicycache(base.ResourceBase):
    pass


class CloudpolicycacheManager(base.StandaloneManager):
    resource_class = Cloudpolicycache
    keyword = 'cloudpolicycache'
    keyword_plural = 'cloudpolicycaches'
    _columns = ["Id", "Name", "Description"]

