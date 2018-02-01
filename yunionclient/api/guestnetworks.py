import yunionclient

from yunionclient.common import base


class GuestnetworkManager(base.JointManager):
    keyword = 'guestnetwork'
    keyword_plural = 'guestnetworks'
    _columns = ['Guest_ID', 'Guest', 'Network_ID', 'Network', 'Mac_addr',
                    'IP_addr', 'Driver', 'BW_limit', 'Index', 'Virtual',
                    'Ifname']

    @classmethod
    def master_class(cls):
        return yunionclient.api.guests.GuestManager

    @classmethod
    def slave_class(cls):
        return yunionclient.api.networks.NetworkManager
