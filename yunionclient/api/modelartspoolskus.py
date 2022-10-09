from yunionclient.common import base

class ModelartsPoolSku(base.ResourceBase):
    pass


class ModelartsPoolSkuManager(base.StandaloneManager):
    resource_class = ModelartsPoolSku
    keyword = 'modelarts_pool_sku'
    keyword_plural = 'modelarts_pool_skus'
    _columns = []