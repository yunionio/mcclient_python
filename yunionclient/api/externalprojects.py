from yunionclient.common import base

class ExternalProject(base.ResourceBase):
    pass

class ExternalProjectManager(base.StandaloneManager):
    resource_class = ExternalProject
    keyword = 'externalproject'
    keyword_plural = 'externalprojects'
    _columns = ["ID", "Name", "Status"]
    _admin_columns = []
