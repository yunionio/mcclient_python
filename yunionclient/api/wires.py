from yunionclient.common import base


class WireManager(base.StandaloneManager):
    keyword = 'wire'
    keyword_plural = 'wires'
    _columns = ['ID', 'Name', 'Bandwidth']
