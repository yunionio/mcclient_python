
from yunionclient.common import base

class DevtoolCronjob(base.ResourceBase):
    pass


class DevtoolCronjobManager(base.StandaloneManager):
    resource_class = DevtoolCronjob
    keyword = 'devtool_cronjob'
    keyword_plural = 'devtool_cronjobs'
    _columns = []
    _admin_columns = []

