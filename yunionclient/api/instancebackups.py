from yunionclient.common import base

class Instancebackup(base.ResourceBase):
    pass


class InstancebackupManager(base.StandaloneManager):
    resource_class = Instancebackup
    keyword = 'instancebackup'
    keyword_plural = 'instancebackups'
    _columns = []