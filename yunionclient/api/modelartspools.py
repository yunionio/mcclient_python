from yunionclient.common import base

class ModelartsPool(base.ResourceBase):
    pass


class ModelartsPoolManager(base.StandaloneManager):
    resource_class = ModelartsPool
    keyword = 'modelarts_pool'
    keyword_plural = 'modelarts_pools'
    _columns = []