
from yunionclient.common import base

class Loadbalancercertificate(base.ResourceBase):
    pass


class LoadbalancercertificateManager(base.StandaloneManager):
    resource_class = Loadbalancercertificate
    keyword = 'loadbalancercertificate'
    keyword_plural = 'loadbalancercertificates'
    _columns = []
    _admin_columns = []

