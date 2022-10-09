from yunionclient.common import base

class Diskbackup(base.ResourceBase):
    pass


class DiskbackupManager(base.StandaloneManager):
    resource_class = Diskbackup
    keyword = 'diskbackup'
    keyword_plural = 'diskbackups'
    _columns = []