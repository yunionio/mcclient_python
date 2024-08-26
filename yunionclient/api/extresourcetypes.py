from yunionclient.common import base

class ExtResourceType(base.ResourceBase):
    pass


class ExtResourceTypeManager(base.ExtdbManager):
    resource_class = ExtResourceType
    keyword = 'ext_resource_type'
    keyword_plural = 'ext_resource_types'
    _columns = ['Id', 'Name']
