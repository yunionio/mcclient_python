
from yunionclient.common import base

class Dbinstancebackup(base.ResourceBase):
    pass


class DbinstancebackupManager(base.StandaloneManager):
    resource_class = Dbinstancebackup
    keyword = 'dbinstancebackup'
    keyword_plural = 'dbinstancebackups'
    _columns = []
    _admin_columns = []

