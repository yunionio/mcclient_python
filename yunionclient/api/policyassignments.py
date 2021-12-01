from yunionclient.common import base

class PolicyAssignment(base.ResourceBase):
    pass


class PolicyAssignmentManager(base.StandaloneManager):
    resource_class = PolicyAssignment
    keyword = 'policy_assignment'
    keyword_plural = 'policy_assignments'
    _columns = ["Id", "Name", "Description"]

