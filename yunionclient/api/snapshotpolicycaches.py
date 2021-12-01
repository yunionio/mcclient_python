
from yunionclient.common import base

class Snapshotpolicycache(base.ResourceBase):
    pass


class SnapshotpolicycacheManager(base.StandaloneManager):
    resource_class = Snapshotpolicycache
    keyword = 'snapshotpolicycache'
    keyword_plural = 'snapshotpolicycaches'
    _columns = []
    _admin_columns = []

