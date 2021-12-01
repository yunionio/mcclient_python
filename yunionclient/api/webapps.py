
from yunionclient.common import base

class Webapp(base.ResourceBase):
    pass


class WebappManager(base.StandaloneManager):
    resource_class = Webapp
    keyword = 'webapp'
    keyword_plural = 'webapps'
    _columns = []
    _admin_columns = []

