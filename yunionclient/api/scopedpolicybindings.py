from yunionclient.common import base

class Scopedpolicybinding(base.ResourceBase):
    pass


class ScopedpolicybindingManager(base.StandaloneManager):
    resource_class = Scopedpolicybinding
    keyword = 'scopedpolicybinding'
    keyword_plural = 'scopedpolicybindings'
    _columns = ["Id", "Policy_Id", "Policy_Name", "Category", "Domain_Id", "Project_Domain", "Project_Id", "Project", "Priority"]

