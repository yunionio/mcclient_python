import yunionclient

from yunionclient.common import base

class CloudproviderregionManager(base.JointManager):
    keyword = 'cloudproviderregion'
    keyword_plural = 'cloudproviderregions'
    _columns = ["Row_Id", "RegionId", "Cloudprovider", "Cloudprovider_Id", "Sync_Status"]


    @classmethod
    def master_class(cls):
        return yunionclient.api.cloudproviders.CloudproviderManager

    @classmethod
    def slave_class(cls):
        return yunionclient.api.cloudregions.CloudregionManager
