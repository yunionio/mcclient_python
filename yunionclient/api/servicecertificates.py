
from yunionclient.common import base

class Servicecertificate(base.ResourceBase):
    pass


class ServicecertificateManager(base.StandaloneManager):
    resource_class = Servicecertificate
    keyword = 'servicecertificate'
    keyword_plural = 'servicecertificates'
    _columns = []
    _admin_columns = []

