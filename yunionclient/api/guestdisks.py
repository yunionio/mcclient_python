import yunionclient

from yunionclient.common import base


class GuestdiskManager(base.JointManager):
    keyword = 'guestdisk'
    keyword_plural = 'guestdisks'
    _columns = ['Guest_ID', 'Guest', 'Disk_ID', 'Disk', 'Disk_size',
                        'Driver', 'Cache_mode', 'Index', 'Status']

    @classmethod
    def master_class(cls):
        return yunionclient.api.guests.GuestManager

    @classmethod
    def slave_class(cls):
        return yunionclient.api.disks.DiskManager
