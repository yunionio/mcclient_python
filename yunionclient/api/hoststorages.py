import yunionclient

from yunionclient.common import base


class HoststorageManager(base.JointManager):
    keyword        = 'hoststorage'
    keyword_plural = 'hoststorages'
    _columns = ['Host_ID', 'Host', 'Storage_ID', 'Storage', 'Mount_point',
                'Capacity', 'Used_capacity', 'Waste_capacity', 'Free_capacity']

    @classmethod
    def master_class(cls):
        return yunionclient.api.hosts.HostManager

    @classmethod
    def slave_class(cls):
        return yunionclient.api.storages.StorageManager
