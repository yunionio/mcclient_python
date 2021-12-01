
from yunionclient.common import base

class Federatedrolebinding(base.ResourceBase):
    pass


class FederatedrolebindingManager(base.StandaloneManager):
    resource_class = Federatedrolebinding
    keyword = 'federatedrolebinding'
    keyword_plural = 'federatedrolebindings'
    _columns = []
    _admin_columns = []

