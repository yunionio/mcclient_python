
from yunionclient.common import base

class Ingress(base.ResourceBase):
    pass


class IngressManager(base.StandaloneManager):
    resource_class = Ingress
    keyword = 'ingress'
    keyword_plural = 'ingresses'
    _columns = []
    _admin_columns = []

