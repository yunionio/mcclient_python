from yunionclient.common import base


class ZoneManager(base.StandaloneManager):
    _columns = ['ID', 'Name', 'Name_cn', 'Status']
    _admin_columns = ['Manager_URI']
    keyword = 'zone'
    keyword_plural = 'zones'
