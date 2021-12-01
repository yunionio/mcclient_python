
from yunionclient.common import base

class Serviceurl(base.ResourceBase):
    pass


class ServiceurlManager(base.StandaloneManager):
    resource_class = Serviceurl
    keyword = 'serviceurl'
    keyword_plural = 'serviceurls'
    _columns = []
    _admin_columns = []

