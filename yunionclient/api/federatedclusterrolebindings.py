
from yunionclient.common import base

class Federatedclusterrolebinding(base.ResourceBase):
    pass


class FederatedclusterrolebindingManager(base.StandaloneManager):
    resource_class = Federatedclusterrolebinding
    keyword = 'federatedclusterrolebinding'
    keyword_plural = 'federatedclusterrolebindings'
    _columns = []
    _admin_columns = []

