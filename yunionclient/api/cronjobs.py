
from yunionclient.common import base

class Cronjob(base.ResourceBase):
    pass


class CronjobManager(base.StandaloneManager):
    resource_class = Cronjob
    keyword = 'cronjob'
    keyword_plural = 'cronjobs'
    _columns = []
    _admin_columns = []

