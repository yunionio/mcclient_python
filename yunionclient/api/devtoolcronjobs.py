from yunionclient.common import base

class DevtoolCronjob(base.ResourceBase):
    pass


class DevtoolCronjobManager(base.StandaloneManager):
    resource_class = DevtoolCronjob
    keyword = 'devtool_cronjob'
    keyword_plural = 'devtool_cronjobs'
    _columns = ["Id", "Ansible_Playbook_Id", "Template_Id", "Server_Id", "Name", "Day", "Hour", "Min", "Sec", "Interval", "Start", "Enabled", "Created_At"]

