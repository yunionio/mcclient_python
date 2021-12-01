from yunionclient.common import base

class Snapshot(base.ResourceBase):
    pass


class SnapshotManager(base.StandaloneManager):
    resource_class = Snapshot
    keyword = 'snapshot'
    keyword_plural = 'snapshots'
    _columns = ["Id", "Name", "Size", "Status", "Disk_Id", "Guest_Id", "Created_At", "Storage_Id", "Storage_Type", "Create_By", "Location", "Out_Of_Chain", "Disk_Type", "Provider"]

