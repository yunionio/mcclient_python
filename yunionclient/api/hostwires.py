import yunionclient

from yunionclient.common import base


class HostwireManager(base.JointManager):
    keyword = 'hostwire'
    keyword_plural = 'hostwires'
    _columns = ['Host_ID', 'Wire_ID', 'Bridge', 'Interface']

    @classmethod
    def master_class(cls):
        return yunionclient.api.hosts.HostManager

    @classmethod
    def slave_class(cls):
        return yunionclient.api.wires.WireManager
