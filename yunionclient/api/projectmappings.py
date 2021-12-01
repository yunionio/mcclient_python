from yunionclient.common import base

class ProjectMapping(base.ResourceBase):
    pass


class ProjectMappingManager(base.StandaloneManager):
    resource_class = ProjectMapping
    keyword = 'project_mapping'
    keyword_plural = 'project_mappings'
    _columns = ["Id", "Name", "Enabled", "Status", "Public_Scope", "Domain_Id", "Domain", "Rules", "Accounts", "Metadata"]

