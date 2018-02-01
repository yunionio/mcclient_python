from yunionclient.common import base


class ReservedIPManager(base.StandaloneManager):
    keyword = 'reservedip'
    keyword_plural = 'reservedips'
    _columns = ['Network_ID', 'Network', 'IP_addr', 'Notes']
