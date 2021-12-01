
from yunionclient.common import base

class NatSku(base.ResourceBase):
    pass


class NatSkuManager(base.StandaloneManager):
    resource_class = NatSku
    keyword = 'nat_sku'
    keyword_plural = 'nat_skus'
    _columns = []
    _admin_columns = []

