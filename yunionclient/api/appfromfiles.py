from yunionclient.common import base

class Appfromfile(base.ResourceBase):
    pass


class AppfromfileManager(base.StandaloneManager):
    resource_class = Appfromfile
    keyword = 'appfromfile'
    keyword_plural = 'appfromfiles'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Namespace_Id", "Namespace", "Labels", "Cluster_Id", "Cluster"]

