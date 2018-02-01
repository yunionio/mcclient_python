import yunionclient

from yunionclient.common import base


class GroupguestManager(base.JointManager):
    keyword = 'groupguest'
    keyword_plural = 'groupguests'
    _columns = ['Group_ID', 'Group', 'Guest_ID', 'Guest', 'IPs', 'Status', 'TAG']

    @classmethod
    def master_class(cls):
        return yunionclient.api.groups.GroupManager

    @classmethod
    def slave_class(cls):
        return yunionclient.api.guests.GuestManager
