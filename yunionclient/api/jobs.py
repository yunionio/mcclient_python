from yunionclient.common import base

class Job(base.ResourceBase):
    pass


class JobManager(base.StandaloneManager):
    resource_class = Job
    keyword = 'job'
    keyword_plural = 'jobs'
    _columns = ["Name", "Id", "Status", "Creationtimestamp", "Created_At", "Namespace_Id", "Namespace", "Labels", "Cluster_Id", "Cluster"]

