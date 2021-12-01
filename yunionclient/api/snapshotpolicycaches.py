from yunionclient.common import base

class Snapshotpolicycache(base.ResourceBase):
    pass


class SnapshotpolicycacheManager(base.StandaloneManager):
    resource_class = Snapshotpolicycache
    keyword = 'snapshotpolicycache'
    keyword_plural = 'snapshotpolicycaches'
    _columns = ["Snapshotpolicy_Id", "External_Id", "Cloudregion_Id", "Manager_Id"]

