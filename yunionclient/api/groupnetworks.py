import yunionclient

from yunionclient.common import base


class GroupnetworkManager(base.JointManager):
    keyword = 'groupnetwork'
    keyword_plural = 'groupnetworks'
    _columns = ['Group_ID', 'Group', 'Network_ID', 'Network', 'Net_mask',
                'IP_addr', 'EIP_addr', 'Index']

    @classmethod
    def master_class(cls):
        return yunionclient.api.groups.GroupManager

    @classmethod
    def slave_class(cls):
        return yunionclient.api.networks.NetworkManager
