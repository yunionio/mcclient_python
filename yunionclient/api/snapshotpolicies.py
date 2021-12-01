from yunionclient.common import base

class Snapshotpolicy(base.ResourceBase):
    pass


class SnapshotpolicyManager(base.StandaloneManager):
    resource_class = Snapshotpolicy
    keyword = 'snapshotpolicy'
    keyword_plural = 'snapshotpolicies'
    _columns = ["Id", "Name", "Status", "Retention_Days", "Repeat_Weekdays", "Time_Points"]

