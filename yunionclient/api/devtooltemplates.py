from yunionclient.common import base

class DevtoolTemplate(base.ResourceBase):
    pass


class DevtoolTemplateManager(base.StandaloneManager):
    resource_class = DevtoolTemplate
    keyword = 'devtool_template'
    keyword_plural = 'devtool_templates'
    _columns = ["Id", "Name", "Domain_Id", "Tenant_Id", "Day", "Hour", "Min", "Sec", "Interval", "Start", "Enabled", "Description", "Is_System"]

