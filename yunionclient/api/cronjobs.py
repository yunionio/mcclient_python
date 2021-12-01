from yunionclient.common import base

class Cronjob(base.ResourceBase):
    pass


class CronjobManager(base.StandaloneManager):
    resource_class = Cronjob
    keyword = 'cronjob'
    keyword_plural = 'cronjobs'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Namespace_Id", "Namespace", "Labels", "Cluster_Id", "Cluster"]

