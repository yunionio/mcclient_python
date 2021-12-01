
from yunionclient.common import base

class ProjectMapping(base.ResourceBase):
    pass


class ProjectMappingManager(base.StandaloneManager):
    resource_class = ProjectMapping
    keyword = 'project_mapping'
    keyword_plural = 'project_mappings'
    _columns = []
    _admin_columns = []

