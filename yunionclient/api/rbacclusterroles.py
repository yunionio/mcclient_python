from yunionclient.common import base

class Rbacclusterrole(base.ResourceBase):
    pass


class RbacclusterroleManager(base.StandaloneManager):
    resource_class = Rbacclusterrole
    keyword = 'rbacclusterrole'
    keyword_plural = 'rbacclusterroles'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Cluster_Id", "Cluster", "Cluster_Id", "Cluster"]

