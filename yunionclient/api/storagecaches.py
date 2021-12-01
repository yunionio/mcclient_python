
from yunionclient.common import base

class Storagecache(base.ResourceBase):
    pass


class StoragecacheManager(base.StandaloneManager):
    resource_class = Storagecache
    keyword = 'storagecache'
    keyword_plural = 'storagecaches'
    _columns = []
    _admin_columns = []

