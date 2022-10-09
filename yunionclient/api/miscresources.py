from yunionclient.common import base

class MiscResource(base.ResourceBase):
    pass


class MiscResourceManager(base.StandaloneManager):
    resource_class = MiscResource
    keyword = 'misc_resource'
    keyword_plural = 'misc_resources'
    _columns = []