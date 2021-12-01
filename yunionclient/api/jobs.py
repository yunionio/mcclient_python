
from yunionclient.common import base

class Job(base.ResourceBase):
    pass


class JobManager(base.StandaloneManager):
    resource_class = Job
    keyword = 'job'
    keyword_plural = 'jobs'
    _columns = []
    _admin_columns = []

