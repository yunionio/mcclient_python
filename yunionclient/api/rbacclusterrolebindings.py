from yunionclient.common import base

class Rbacclusterrolebinding(base.ResourceBase):
    pass


class RbacclusterrolebindingManager(base.StandaloneManager):
    resource_class = Rbacclusterrolebinding
    keyword = 'rbacclusterrolebinding'
    keyword_plural = 'rbacclusterrolebindings'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Cluster_Id", "Cluster", "Cluster_Id", "Cluster"]

