
from yunionclient.common import base

class Servertemplate(base.ResourceBase):
    pass


class ServertemplateManager(base.StandaloneManager):
    resource_class = Servertemplate
    keyword = 'servertemplate'
    keyword_plural = 'servertemplates'
    _columns = []
    _admin_columns = []

