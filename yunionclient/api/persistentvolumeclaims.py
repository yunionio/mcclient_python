from yunionclient.common import base

class Persistentvolumeclaim(base.ResourceBase):
    pass


class PersistentvolumeclaimManager(base.StandaloneManager):
    resource_class = Persistentvolumeclaim
    keyword = 'persistentvolumeclaim'
    keyword_plural = 'persistentvolumeclaims'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Namespace_Id", "Namespace", "Labels", "Volume", "Storageclass", "Mountedby", "Cluster_Id", "Cluster"]

