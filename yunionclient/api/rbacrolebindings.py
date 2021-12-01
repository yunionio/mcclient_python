from yunionclient.common import base

class Rbacrolebinding(base.ResourceBase):
    pass


class RbacrolebindingManager(base.StandaloneManager):
    resource_class = Rbacrolebinding
    keyword = 'rbacrolebinding'
    keyword_plural = 'rbacrolebindings'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Namespace_Id", "Namespace", "Labels", "Cluster_Id", "Cluster"]

