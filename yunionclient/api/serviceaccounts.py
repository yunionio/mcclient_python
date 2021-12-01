from yunionclient.common import base

class Serviceaccount(base.ResourceBase):
    pass


class ServiceaccountManager(base.StandaloneManager):
    resource_class = Serviceaccount
    keyword = 'serviceaccount'
    keyword_plural = 'serviceaccounts'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Namespace_Id", "Namespace", "Labels", "Cluster_Id", "Cluster"]

