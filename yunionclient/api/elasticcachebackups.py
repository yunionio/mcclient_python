from yunionclient.common import base

class Elasticcachebackup(base.ResourceBase):
    pass


class ElasticcachebackupManager(base.StandaloneManager):
    resource_class = Elasticcachebackup
    keyword = 'elasticcachebackup'
    keyword_plural = 'elasticcachebackups'
    _columns = ["Id", "Name", "Description"]

