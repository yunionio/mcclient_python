
from yunionclient.common import base

class Rbacrolebinding(base.ResourceBase):
    pass


class RbacrolebindingManager(base.StandaloneManager):
    resource_class = Rbacrolebinding
    keyword = 'rbacrolebinding'
    keyword_plural = 'rbacrolebindings'
    _columns = []
    _admin_columns = []

