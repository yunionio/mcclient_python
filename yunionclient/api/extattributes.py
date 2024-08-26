from yunionclient.common import base

class ExtAttribute(base.ResourceBase):
    pass


class ExtAttributeManager(base.ExtdbManager):
    resource_class = ExtAttribute
    keyword = 'ext_attribute'
    keyword_plural = 'ext_attributes'
    _columns = ['Id', 'Name']
