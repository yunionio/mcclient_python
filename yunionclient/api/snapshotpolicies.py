
from yunionclient.common import base

class Snapshotpolicy(base.ResourceBase):
    pass


class SnapshotpolicyManager(base.StandaloneManager):
    resource_class = Snapshotpolicy
    keyword = 'snapshotpolicy'
    keyword_plural = 'snapshotpolicies'
    _columns = []
    _admin_columns = []

