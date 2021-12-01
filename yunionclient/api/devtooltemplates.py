
from yunionclient.common import base

class DevtoolTemplate(base.ResourceBase):
    pass


class DevtoolTemplateManager(base.StandaloneManager):
    resource_class = DevtoolTemplate
    keyword = 'devtool_template'
    keyword_plural = 'devtool_templates'
    _columns = []
    _admin_columns = []

