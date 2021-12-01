
from yunionclient.common import base

class Rolepolicy(base.ResourceBase):
    pass


class RolepolicyManager(base.StandaloneManager):
    resource_class = Rolepolicy
    keyword = 'rolepolicy'
    keyword_plural = 'rolepolicies'
    _columns = []
    _admin_columns = []

