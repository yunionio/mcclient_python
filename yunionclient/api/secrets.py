
from yunionclient.common import base

class Secret(base.ResourceBase):
    pass


class SecretManager(base.StandaloneManager):
    resource_class = Secret
    keyword = 'secret'
    keyword_plural = 'secrets'
    _columns = []
    _admin_columns = []

