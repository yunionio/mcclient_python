from yunionclient.common import base

class X509keypair(base.ResourceBase):
    pass


class X509keypairManager(base.StandaloneManager):
    resource_class = X509keypair
    keyword = 'x509keypair'
    keyword_plural = 'x509keypairs'
    _columns = ["Name", "Id", "Status", "User", "Certificate", "Private_Key", "Cluster", "Cluster_Id"]

