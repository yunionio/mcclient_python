from yunionclient.common import base

class Cloudproviderregion(base.ResourceBase):
    pass


class CloudproviderregionManager(base.StandaloneManager):
    resource_class = Cloudproviderregion
    keyword = 'cloudproviderregion'
    keyword_plural = 'cloudproviderregions'
    _columns = ["Row_Id", "RegionId", "Cloudprovider", "Cloudprovider_Id", "Sync_Status"]

