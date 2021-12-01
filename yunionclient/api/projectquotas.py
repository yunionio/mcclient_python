from yunionclient.common import base

class ProjectQuota(base.ResourceBase):
    pass


class ProjectQuotaManager(base.StandaloneManager):
    resource_class = ProjectQuota
    keyword = 'project_quota'
    keyword_plural = 'project_quotas'
    _columns = ["Id", "Name", "Description"]

