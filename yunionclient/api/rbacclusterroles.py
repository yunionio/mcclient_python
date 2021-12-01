
from yunionclient.common import base

class Rbacclusterrole(base.ResourceBase):
    pass


class RbacclusterroleManager(base.StandaloneManager):
    resource_class = Rbacclusterrole
    keyword = 'rbacclusterrole'
    keyword_plural = 'rbacclusterroles'
    _columns = []
    _admin_columns = []

