from yunionclient.common import base

class Backupstorage(base.ResourceBase):
    pass


class BackupstorageManager(base.StandaloneManager):
    resource_class = Backupstorage
    keyword = 'backupstorage'
    keyword_plural = 'backupstorages'
    _columns = []