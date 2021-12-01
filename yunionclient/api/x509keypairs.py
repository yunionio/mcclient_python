
from yunionclient.common import base

class X509keypair(base.ResourceBase):
    pass


class X509keypairManager(base.StandaloneManager):
    resource_class = X509keypair
    keyword = 'x509keypair'
    keyword_plural = 'x509keypairs'
    _columns = []
    _admin_columns = []

