from yunionclient.common import base

class Cloudpermission(base.ResourceBase):
    pass


class CloudpermissionManager(base.CloudidManager):
    resource_class = Cloudpermission
    keyword = 'cloudpermission'
    keyword_plural = 'cloudpermissions'
    _columns = []