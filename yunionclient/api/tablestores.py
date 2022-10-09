from yunionclient.common import base

class Tablestore(base.ResourceBase):
    pass


class TablestoreManager(base.StandaloneManager):
    resource_class = Tablestore
    keyword = 'tablestore'
    keyword_plural = 'tablestores'
    _columns = []