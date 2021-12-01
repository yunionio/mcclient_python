
from yunionclient.common import base

class DbinstanceSku(base.ResourceBase):
    pass


class DbinstanceSkuManager(base.StandaloneManager):
    resource_class = DbinstanceSku
    keyword = 'dbinstance_sku'
    keyword_plural = 'dbinstance_skus'
    _columns = []
    _admin_columns = []

