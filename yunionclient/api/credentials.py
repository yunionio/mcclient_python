
from yunionclient.common import base

class Credential(base.ResourceBase):
    pass


class CredentialManager(base.StandaloneManager):
    resource_class = Credential
    keyword = 'credential'
    keyword_plural = 'credentials'
    _columns = []
    _admin_columns = []

