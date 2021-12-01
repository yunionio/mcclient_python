
from yunionclient.common import base

class IdentityProvider(base.ResourceBase):
    pass


class IdentityProviderManager(base.StandaloneManager):
    resource_class = IdentityProvider
    keyword = 'identity_provider'
    keyword_plural = 'identity_providers'
    _columns = []
    _admin_columns = []

