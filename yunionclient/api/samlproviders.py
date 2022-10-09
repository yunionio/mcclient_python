from yunionclient.common import base

class SamlProvider(base.ResourceBase):
    pass


class SamlProviderManager(base.CloudidManager):
    resource_class = SamlProvider
    keyword = 'saml_provider'
    keyword_plural = 'saml_providers'
    _columns = []