from yunionclient.common import base

class Persistentvolume(base.ResourceBase):
    pass


class PersistentvolumeManager(base.StandaloneManager):
    resource_class = Persistentvolume
    keyword = 'persistentvolume'
    keyword_plural = 'persistentvolumes'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Storageclass", "Claim", "Accessmodes", "Cluster_Id", "Cluster"]

