from yunionclient.common import base

class Storagecache(base.ResourceBase):
    pass


class StoragecacheManager(base.StandaloneManager):
    resource_class = Storagecache
    keyword = 'storagecache'
    keyword_plural = 'storagecaches'
    _columns = ["Id", "Name", "Path", "Storages", "Size", "Count"]

