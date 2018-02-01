import yunionclient

from yunionclient.common import base


class BaremetalstorageManager(base.JointManager):
    keyword = 'baremetalstorage'
    keyword_plural = 'baremetalstorages'
    _columns = ['Baremetal_ID', 'Storage_ID', 'Config', 'Real_capacity']

    @classmethod
    def master_class(cls):
        return yunionclient.api.baremetals.BaremetalManager

    @classmethod
    def slave_class(cls):
        return yunionclient.api.storages.StorageManager
