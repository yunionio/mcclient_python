
from yunionclient.common import base

class Snapshot(base.ResourceBase):
    pass


class SnapshotManager(base.StandaloneManager):
    resource_class = Snapshot
    keyword = 'snapshot'
    keyword_plural = 'snapshots'
    _columns = []
    _admin_columns = []

