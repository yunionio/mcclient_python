import yunionclient

from yunionclient.common import base


class EdgewireManager(base.JointManager):
    keyword = 'edgewire'
    keyword_plural = 'edgewires'
    _columns = ['Edge_ID', 'Wire_ID', 'Edge', 'Wire']

    @classmethod
    def master_class(cls):
        return yunionclient.api.edges.EdgeManager

    @classmethod
    def slave_class(cls):
        return yunionclient.api.wires.WireManager
