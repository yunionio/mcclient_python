
from yunionclient.common import base

class Cachedloadbalancercertificate(base.ResourceBase):
    pass


class CachedloadbalancercertificateManager(base.StandaloneManager):
    resource_class = Cachedloadbalancercertificate
    keyword = 'cachedloadbalancercertificate'
    keyword_plural = 'cachedloadbalancercertificates'
    _columns = []
    _admin_columns = []

