from yunionclient.common import base

class Storageclass(base.ResourceBase):
    pass


class StorageclassManager(base.StandaloneManager):
    resource_class = Storageclass
    keyword = 'storageclass'
    keyword_plural = 'storageclasses'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Provisioner", "Isdefault", "Cluster_Id", "Cluster"]

