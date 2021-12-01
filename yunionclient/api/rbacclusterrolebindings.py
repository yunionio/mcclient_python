
from yunionclient.common import base

class Rbacclusterrolebinding(base.ResourceBase):
    pass


class RbacclusterrolebindingManager(base.StandaloneManager):
    resource_class = Rbacclusterrolebinding
    keyword = 'rbacclusterrolebinding'
    keyword_plural = 'rbacclusterrolebindings'
    _columns = []
    _admin_columns = []

