import yunionclient

from yunionclient.common import base


class BaremetalnetworkManager(base.JointManager):
    keyword = 'baremetalnetwork'
    keyword_plural = 'baremetalnetworks'
    _columns = ['Baremetal_ID', 'Network_ID', 'IP_addr', 'Mac_addr']

    @classmethod
    def master_class(cls):
        return yunionclient.api.baremetals.BaremetalManager

    @classmethod
    def slave_class(cls):
        return yunionclient.api.networks.NetworkManager
