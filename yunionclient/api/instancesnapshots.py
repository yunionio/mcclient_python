
from yunionclient.common import base

class InstanceSnapshot(base.ResourceBase):
    pass


class InstanceSnapshotManager(base.StandaloneManager):
    resource_class = InstanceSnapshot
    keyword = 'instance_snapshot'
    keyword_plural = 'instance_snapshots'
    _columns = []
    _admin_columns = []

