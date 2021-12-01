
from yunionclient.common import base

class Appfromfile(base.ResourceBase):
    pass


class AppfromfileManager(base.StandaloneManager):
    resource_class = Appfromfile
    keyword = 'appfromfile'
    keyword_plural = 'appfromfiles'
    _columns = []
    _admin_columns = []

