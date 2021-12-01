from yunionclient.common import base

class Cloudpermission(base.ResourceBase):
    pass


class CloudpermissionManager(base.StandaloneManager):
    resource_class = Cloudpermission
    keyword = 'cloudpermission'
    keyword_plural = 'cloudpermissions'
    _columns = ["Id", "Name", "Description"]

