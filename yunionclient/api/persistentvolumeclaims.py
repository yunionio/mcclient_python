
from yunionclient.common import base

class Persistentvolumeclaim(base.ResourceBase):
    pass


class PersistentvolumeclaimManager(base.StandaloneManager):
    resource_class = Persistentvolumeclaim
    keyword = 'persistentvolumeclaim'
    keyword_plural = 'persistentvolumeclaims'
    _columns = []
    _admin_columns = []

