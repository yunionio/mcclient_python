from yunionclient.common import base

class ExtResource(base.ResourceBase):
    pass


class ExtResourceManager(base.ExtdbManager):
    resource_class = ExtResource
    keyword = 'ext_resource'
    keyword_plural = 'ext_resources'
    _columns = ['Id', 'ResourceType']
