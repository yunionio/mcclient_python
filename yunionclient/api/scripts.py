from yunionclient.common import base

class Script(base.ResourceBase):
    pass


class ScriptManager(base.StandaloneManager):
    resource_class = Script
    keyword = 'script'
    keyword_plural = 'scripts'
    _columns = ["Id", "Name", "Type", "Playbook_Reference", "Max_Try_Times"]

