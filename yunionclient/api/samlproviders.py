
from yunionclient.common import base

class SamlProvider(base.ResourceBase):
    pass


class SamlProviderManager(base.StandaloneManager):
    resource_class = SamlProvider
    keyword = 'saml_provider'
    keyword_plural = 'saml_providers'
    _columns = []
    _admin_columns = []

