from yunionclient.common import base


class Vpc(base.ResourceBase):
    pass


class VpcManager(base.StandaloneManager):
    resource_class = Vpc
    keyword = 'vpc'
    keyword_plural = 'vpcs'
    _columns = ['ID', 'Name', 'CloudRegion_Id']
