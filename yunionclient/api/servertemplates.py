from yunionclient.common import base

class Servertemplate(base.ResourceBase):
    pass


class ServertemplateManager(base.StandaloneManager):
    resource_class = Servertemplate
    keyword = 'servertemplate'
    keyword_plural = 'servertemplates'
    _columns = ["Id", "Name", "Public_Scope", "Is_Public", "Project_Id", "Content"]

